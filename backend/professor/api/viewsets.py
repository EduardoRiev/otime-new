from rest_framework.viewsets import ModelViewSet
from professor.models import Professor
from .serializers import professorSerializer

class professorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = professorSerializer
