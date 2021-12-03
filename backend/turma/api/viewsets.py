from rest_framework.viewsets import ModelViewSet
from turma.models import Turma
from .serializers import TurmaSerializer

class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    