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