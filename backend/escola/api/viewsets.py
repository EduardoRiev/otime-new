from rest_framework.viewsets import ModelViewSet
from escola.models import Escola
from .serializers import escolaSerializer

class escolaViewSet(ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = escolaSerializer
