from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)
    
    #first element gets none
    exists = Product.objects.filter(pk=0).first()

    #get boolean
    exists = Product.objects.filter(pk=0).exists()

    return render(request, 'hello.html', {'name': 'Asib'})
