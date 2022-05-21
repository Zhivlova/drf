from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO
from .serializers import ProjectModelSerializer, TODOModelSerializer
from django_filters import rest_framework as filters


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination


class TODOLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    filterset_fields = ['create_date', 'update_date']
    pagination_class = TODOLimitOffsetPagination


class ProjectFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['title']


class TODOFilter(filters.FilterSet):
    todo_project = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = TODO
        fields = ['todo_project']


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
