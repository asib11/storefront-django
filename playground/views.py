from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
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
    # query_set = Product.objects.filter(title__icontains = 'coffee') #can filter by string

    # complex filtering look up using Q
    # query_set = Product.objects.filter(inventory__lt = 10, unit_price__lt = 20)
    # query_set = Product.objects.filter(inventory__lt = 10).filter( unit_price__lt = 20) #another way

    # using Q when we need to OR operator use, ~ = use for not or negleting value
    # query_set = Product.objects.filter(Q(inventory__lt = 10) | Q(unit_price__lt = 20))
    # query_set = Product.objects.filter(Q(inventory__lt = 10) | ~Q(unit_price__lt = 20))
    query_set = Product.objects.filter(Q(inventory__lt = 10) & ~Q(unit_price__lt = 20))
    

    return render(request, 'hello.html', {'name': 'Asib', 'products': list(query_set)})
