from rest_framework.serializers import ModelSerializer
from card.models import Card

class cardSerializer(ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'
