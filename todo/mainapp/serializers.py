from typing import Type

from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User, Client


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ClientModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
