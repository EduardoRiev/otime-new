from rest_framework.viewsets import ModelViewSet
from disciplina.models import Disciplina
from .serializers import disciplinaSerializer

class disciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = disciplinaSerializer
