import pickle
import tensorflow as tf
from pathlib import Path
from django.apps import AppConfig
from langchain.llms import OpenAI


class DermaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'derma'
    lesionModel = tf.keras.models.load_model(Path('models/my_model.h5').resolve())
    resolve = Path('models/picke_model.pkl').resolve()
    diseaseModel = pickle.load(open(resolve, 'rb'))
    llm = OpenAI(temperature=0)
