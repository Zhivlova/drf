from rest_framework.viewsets import ModelViewSet
from .models import User, Header, Footer
from .serializers import UserModelSerializer, HeaderModelSerializer, FooterModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class HeaderModelViewSet(ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderModelSerializer


class FooterModelViewSet(ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterModelSerializer
