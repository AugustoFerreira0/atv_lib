from rest_framework import viewsets
from .models import Carro, Moto
from .serializers import CarroSerializers, MotoSerializers

class CarroViewset(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializers

class MotoViewset(viewsets.ModelViewSet):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializers