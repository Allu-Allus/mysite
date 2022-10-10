
from django.urls import path,include
from .views import index, my_place , new_one

urlpatterns = [
    path('',index),
      path('new',new_one),
      path('place',my_place)
]