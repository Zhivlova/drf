from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Client


class ClientModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
