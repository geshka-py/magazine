from django.urls import path
from .views import catalog, ajax_cart


urlpatterns = [
    path('', catalog),
    path('ajax_cart', ajax_cart)
]