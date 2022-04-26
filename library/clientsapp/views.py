from rest_framework.viewsets import ModelViewSet
from .models import Client
from .serializers import ClientModelSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer
