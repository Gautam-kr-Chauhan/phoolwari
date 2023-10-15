from django.urls import path
from flower.views import all_flowers
urlpatterns = [
    path('all_flowers/',all_flowers,name='all_flowers')  
]
