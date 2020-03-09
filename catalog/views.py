from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from cart.models import Order


def catalog(request):
    data = dict()
    goods = Product.objects.all()
    data['goods'] = goods
    return render(request, 'catalog/index.html', context=data)


def ajax_cart(request):
    response = dict()
    pid = request.GET['pid']
    uid = request.user.id
    sid = 1
    _count = 1
    Order.objects.create(count=_count, status_id=sid, product_id=pid, user_id=uid)
    response['mess'] = f'Заказ успешно сохранен для {request.user.username}'
    return JsonResponse(response)
