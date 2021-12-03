from rest_framework.serializers import ModelSerializer
from professor.models import Professor

class professorSerializer(ModelSerializer):

    class Meta:
        model = Professor
        fields = '__all__'
