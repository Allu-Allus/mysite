
from tempfile import template
from turtle import update
from django.urls import path,include
from .views import register
from django.contrib.auth import views as authentication_views

app_name = 'users'

urlpatterns = [
  
    path('register/', register,name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    # path('products/<int:id>',product_details,name='product_details'),
    # path('products/add',add_product,name='add_product'),
    # path('products/update/<int:id>',update_product,name='update_product'),
    # path('products/delete/<int:id>',delete_product,name='delete_product'),
] 