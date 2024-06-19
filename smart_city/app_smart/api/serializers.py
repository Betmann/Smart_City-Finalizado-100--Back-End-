from django.contrib.auth.models import User
from rest_framework import serializers
from app_smart.models import Sensor, TemperaturaData, UmidadeData, LuminosidadeData, ContadorData
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # A senha só é usada para escrita

    def create(self, validated_data):
        # Criptografa a senha antes de salvar o usuário
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # Adicione outros campos se necessário
        extra_kwargs = {'password': {'write_only': True}}

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'  # Serializa todos os campos do modelo Sensor

class TemperaturaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperaturaData
        fields = '__all__'  # Serializa todos os campos do modelo TemperaturaData

class UmidadeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmidadeData
        fields = '__all__'  # Serializa todos os campos do modelo UmidadeData

class LuminosidadeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuminosidadeData
        fields = '__all__'  # Serializa todos os campos do modelo LuminosidadeData

class ContadorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContadorData
        fields = '__all__'  # Serializa todos os campos do modelo ContadorData
