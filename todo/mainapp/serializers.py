from typing import Type

from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User, Header, Footer


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class HeaderModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'


class FooterModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'
