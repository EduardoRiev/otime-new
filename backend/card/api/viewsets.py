from rest_framework.viewsets import ModelViewSet
from card.models import Card
from .serializers import cardSerializer


class cardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = cardSerializer
    filterset_fields = ['sala', 'disciplina', 'turma', 'dia', 'horario']
