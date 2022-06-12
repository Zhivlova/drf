from typing import Type

from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project, TODO

class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TODOModelSerializer(ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
