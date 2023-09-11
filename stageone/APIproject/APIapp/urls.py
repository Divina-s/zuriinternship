from django.urls import path
from .views import my_endpoint
urlpatterns = [    path('myendpoint/', my_endpoint, name='my_endpoint'),]