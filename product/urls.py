from django.urls import path, re_path
from .views import product, ajax_product, upload_basket, edit


urlpatterns = [
    path('', product),
    path('product', product),
    path('<int:product_id>', product, name='product'),
    path('ajax_product', ajax_product),
    path('upload_basket', upload_basket),
    re_path(r'^edit/(?P<oid>[0-9]+)$', edit),
]