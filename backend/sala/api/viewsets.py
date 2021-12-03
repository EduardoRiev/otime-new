from rest_framework.viewsets import ModelViewSet
from sala.models import Sala, Tipo, Ferramenta
from .serializers import salaSerializer, tipoSerializer, ferramentaSerializer

class salaViewSet(ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = salaSerializer

class tipoViewSet(ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = tipoSerializer

class ferramentaViewSet(ModelViewSet):
    queryset = Ferramenta.objects.all()
    serializer_class = ferramentaSerializer
