from rest_framework.serializers import ModelSerializer
from sala.models import Sala, Tipo, Ferramenta

class salaSerializer(ModelSerializer):

    class Meta:
        model = Sala
        fields = '__all__'

class tipoSerializer(ModelSerializer):

    class Meta:
        model =  Tipo
        fields = '__all__'

class ferramentaSerializer(ModelSerializer):

    class Meta:
        model = Ferramenta
        fields = '__all__'