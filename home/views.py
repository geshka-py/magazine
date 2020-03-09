from django.shortcuts import render
from catalog.models import Product


def index(request):
    data = dict()
    goods1 = Product.objects.all()
    goods = goods1[:8]
    data['goods'] = goods
    return render(request, 'home/index.html', context=data)


def about(request):
    return render(request, 'home/about.html')
