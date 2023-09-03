from rest_framework import serializers
from .models import Carro, Moto

class CarroSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Carro
        fields = '__all__'

class MotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'
