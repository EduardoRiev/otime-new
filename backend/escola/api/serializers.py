from rest_framework.serializers import ModelSerializer
from escola.models import Escola

class escolaSerializer(ModelSerializer):

    class Meta:
        model = Escola
        fields = '__all__'
