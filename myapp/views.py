from django.http import HttpResponse

# Create your views here.
def index(request):
    d = {
        "name":"Allu",
        "age":"24" ,
    }
    return HttpResponse("<b>Hello World</b>")