from rest_framework import serializers
from derma.models import LesionRequest, LesionResponse


class LesionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LesionRequest
        fields = '__all__'


class LesionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LesionResponse
        exclude = ('id',)
