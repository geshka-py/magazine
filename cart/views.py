from django.shortcuts import render, redirect
from .models import Order

# from .forms import OrderForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    uid = request.user.id
    orders = Order.objects.filter(user_id=uid)
    data = dict()
    data['orders'] = orders
    return render(request, 'cart/index.html', context=data)


def delete(request, oid: int):
    data = dict()
    order = Order.objects.get(id=oid)
    if request.method == 'GET':
        order.delete()
        return redirect('/cart')
    elif request.method == 'POST':
        order.delete()
        return redirect('/cart')


def total(request, oid: int):
    data = dict()
    orders = Order.objects.get(id=oid)
    total_ = 0
    for order in orders:
        total_ += order.count * order.product.price
    return render(request, 'cart/index.html', context=data)


def delete_all(request):
    data = dict()
    order = Order.objects.all()
    data['order'] = order
    order.delete()
    return redirect('/cart')


def confirm(request, oid: int):
    data = dict()
    order = Order.objects.get(id=oid)
    user_name = request.user.username
    user_email = request.user.email
    admin_email = 'softmasterlab@gmail.com'
    am = order.count * order.product.price
    data['am'] = am
    if request.method == 'GET':
        data['order'] = order
        return render(request, 'cart/confirm.html', context=data)
    elif request.method == 'POST':
        # Отправка почтового уведомления на admin_email:
        email = admin_email
        context = 'Сообщение о подтверждении заказа\n'
        context += '--------------------------------\n'
        context += f'Пользователь - {user_name}\n'
        context += f'Товар - {order.product.name}\n'
        context += f'Цена - {order.product.price}\n'
        context += f'Количество - {order.count}\n'
        context += f'Стоимость - {am}\n'
        context += '--------------------------------\n'
        context += f'Обратная связь - {user_email}\n'
        context += '--------------------------------\n'
        send_mail('Подтверждение заказа', context, "itstep.projects@gmail.com",
                  [email], fail_silently=False)
        data['mess'] = 'Заказ успешно принят!\nОжидайте сообщение о сроках и условиях доставки'
        return render(request, 'cart/confirm_res.html', context=data)


