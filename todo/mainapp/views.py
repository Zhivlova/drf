from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import User, Header, Footer
from .serializers import UserModelSerializer, HeaderModelSerializer, FooterModelSerializer, UserModelSerializer2
from rest_framework import viewsets


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]

    def list(self, request):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        from rest_framework.generics import get_object_or_404
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        from rest_framework.generics import get_object_or_404
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)


class HeaderModelViewSet(ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderModelSerializer


class FooterModelViewSet(ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterModelSerializer


class StatusAPIView(ViewSet):
    queryset = User.objects.all()
    serializer = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '1':
            return UserModelSerializer
        return UserModelSerializer2


