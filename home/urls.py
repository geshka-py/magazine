from django.urls import path
from .views import index, about


urlpatterns = [
    path('', index),
    path('index', index),
    path('about', about),
]