import numpy as np
from PIL import Image
import tensorflow as tf
from .apps import DermaConfig
from langchain.chains import LLMChain
from derma.models import LesionResponse
from langchain.prompts import PromptTemplate
from derma.serializers import LesionResponseSerializer


class LesionService:
    def __init__(self):
        self.class_names = {'costras': 1, 'dermatofitosis': 5, 'leucoplasia': 4, 'maculopapular': 6, 'papulas': 2,
                            'vesiculas': 3}

    def predict_lesion(self, image):
        img = Image.open(image)
        img = img.resize((320, 320))
        img = np.expand_dims(img, axis=0)
        predictions = DermaConfig.lesionModel.predict(img)
        score = tf.nn.softmax(predictions[0])
        argmax = np.argmax(score)
        return list(self.class_names)[argmax]

    def format_data_to_predict_format(self, serializer, lesion):
        x = [self.class_names[lesion]]
        for key, value in serializer.data.items():
            if key in ['image', 'cedula', 'nombre']:
                continue
            if isinstance(value, bool):
                x.append({True: 1, False: 0}[value])
                continue
            x.append(value)
        return np.expand_dims(x, axis=0)

    def get_treatment(self, disease: str):
        prompt = PromptTemplate.from_template('Cual seria el mejor tratamiento para esta enfermaedad ${e}?')
        chain = LLMChain(llm=DermaConfig.llm, prompt=prompt)
        return chain.run(e=disease)

    def predict_disease(self, serializer):
        lesion = self.predict_lesion(serializer.validated_data['image'])
        x = self.format_data_to_predict_format(serializer, lesion)
        predictDisease = DermaConfig.diseaseModel.predict(x)
        disease = predictDisease[0]
        treatment = self.get_treatment(disease)
        response = LesionResponse(cedula=serializer.validated_data['cedula'],
                                  nombre=serializer.validated_data['nombre'],
                                  edad=serializer.validated_data['edad'],
                                  lesion=lesion,
                                  enfermedad=disease,
                                  tratamiento=treatment
                                  )
        return LesionResponseSerializer(response).data
