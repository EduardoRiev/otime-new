from rest_framework.serializers import ModelSerializer
from disciplina.models import Disciplina

class disciplinaSerializer(ModelSerializer):

    class Meta:
        model = Disciplina
        fields = '__all__'
