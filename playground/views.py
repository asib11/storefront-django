from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, OrderItem



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
    # query_set = Product.objects.filter(Q(inventory__lt = 10) & ~Q(unit_price__lt = 20))

    # F use for refferce another field, table etc
    # query_set = Product.objects.filter(inventory = F('unit_price'))
    
    #sorting
    # query_set = Product.objects.order_by('unit_price', '-title').reverse()
    # query_set = Product.objects.filter(collection__id = 1).order_by('unit_price')

    #if i want to access single data
    # product = Product.objects.order_by('unit_price')[0]
    # query_set = Product.objects.earliest('unit_price') # alternative to access single data

    # limit
    # query_set = Product.objects.order_by('unit_price', '-title').reverse()[5:10]

    #selecting field to query
    # select product that has been ordered and sort them by title
    query_set = Product.objects.filter(id__in = OrderItem.objects.values('product_id').distinct() ).order_by('title')
    return render(request, 'hello.html', {'name': 'Asib', 'products':list(query_set) })
