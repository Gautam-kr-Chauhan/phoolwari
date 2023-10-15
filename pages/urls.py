from django.urls import path
from pages.views import index,heritage
urlpatterns = [
    path('',index,name='index'),
    path('heritage',heritage,name="heritage"),
]
