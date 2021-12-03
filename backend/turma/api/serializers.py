from rest_framework.serializers import ModelSerializer
from turma.models import Turma

class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'
