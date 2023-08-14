from rest_framework import status
from .service import LesionService
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from derma.serializers import LesionRequestSerializer


class DiseaseView(APIView):

    def __init__(self):
        self.service = LesionService()

    def post(self, request: Request):
        print('entro')
        serializer = LesionRequestSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            result = self.service.predict_disease(serializer)
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(status=400)
