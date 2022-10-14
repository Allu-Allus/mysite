
from django.urls import path,include
from .views import index , new_one, product_details, products

urlpatterns = [
    path('',index),
      path('new/',new_one),
      path('products/', products),
     path('products/<int:id>',product_details)
] 