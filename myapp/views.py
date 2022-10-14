from itertools import product
from myapp.models import Product
from cgitb import html
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
 
# Create your views here.
def index(request):
    d = {
        "name":"Allu",
        "age":"24" ,
    }
    
    li = ["Allen","Sreerag","Alwin","Allu"]

    for i in range(0,10):
        print(i)

    context = {'names': li}

    return render(request, 'myapp/index.html',context=context)

def new_one(request):
    return render(request, 'listing/new_one.html')

def products(request):
    # p = Product.objects.filter(price__gt =100000) 
    p = Product.objects.all()
    context = {'products':p}
    return  render(request, 'myapp/products.html',context=context)

def product_details(request,id):
    p = Product.objects.get(id=id)
    context = {'p':p}
    return render(request,'myapp/product_details.html',context=context)