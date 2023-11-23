from django.urls import path
from flower.views import all_flowers,flower_category
urlpatterns = [
    path('all_flowers/',all_flowers,name='all_flowers'),
    path('flower_category/<int:cid>',flower_category,name='flower_category')  
]
