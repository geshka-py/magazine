from django.urls import path, re_path
from .views import index, delete_all, delete, confirm, total


urlpatterns = [
    path('', index),
    re_path(r'^delete/(?P<oid>[0-9]+)$', delete),
    re_path(r'^confirm/(?P<oid>[0-9]+)$', confirm),
    path('delete_all', delete_all),
    path('confirm', confirm),
    re_path(r'^total/(?P<oid>[0-9]+)$', total),
]