from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)
    
    #first element gets none
    # exists = Product.objects.filter(pk=0).first()

    #get boolean
    # exists = Product.objects.filter(pk=0).exists()

    # query_set = Product.objects.filter(unit_price__range = (20, 30))
    # query_set = Product.objects.filter(collections__id__range = (1, 2, 3))
    query_set = Product.objects.filter(title__icontains = 'coffee') #can filter by string

    return render(request, 'hello.html', {'name': 'Asib', 'products': query_set})
