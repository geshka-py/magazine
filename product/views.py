from django.shortcuts import render, redirect
from catalog.models import Product
from cart.models import Order
from django.http import JsonResponse
from .forms import Form1


def product(request, product_id):
    data = dict()
    product_ = Product.objects.get(id=product_id)
    data['product'] = product_
    return render(request, 'product/product.html', context=data)


def ajax_product(request):
    data2 = dict()
    response = dict()
    pid = request.GET['pid']

    uid = request.user.id
    _count = request.GET.get('cop')

    Order.objects.create(count=_count, product_id=pid, user_id=uid)
    response['mess'] = f'Заказ успешно сохранен для {request.user.username}'
    return render(request, 'product/')


def upload_basket(request):
    response = dict()
    uid = request.user.id
    orders = Order.objects.filter(user_id=uid)
    # Подсчет общей стоимости товаров
    amount = 0
    for order in orders:
        amount += order.count * order.product.price
    response['amount'] = amount
    print(amount)
    # Отправка данных:
    response['test'] = uid
    return JsonResponse(response)


def edit(request, oid: int):
    data = dict()
    order = Product.objects.get(id=oid)
    data['form'] = Form1(instance=product)
    if request.method == 'POST':
        data['price'] = order.product.price
        return render(request, 'product/product.html', context=data)
    elif request.method == 'GET':
        product_form = Form1(request.POST)
        if product_form.is_valid():
            product.price = product_form.cleaned_data['price']
            order.save()

        return redirect('/product/product')

