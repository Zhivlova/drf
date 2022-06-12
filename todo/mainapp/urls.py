from django.urls import path
from .views import StatusAPIView

app_name = 'users'
urlpatterns = [
    path('', StatusAPIView.as_view())
]