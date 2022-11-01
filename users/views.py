from multiprocessing import context
from django.shortcuts import render,redirect
from users.forms import NewUserForm

# Create your views here.

def register(request):

    form = NewUserForm(request.POST)
    if request.method == 'POST':
        # form = NewUserForm(request.POST)
        print(f'Form Valid :{form.is_valid()}')
        if form.is_valid():
            form.save()
        return redirect('/myapp/products')
        
    
    context = {
        'form': form,
    }

    return render(request, 'users/register.html',context)