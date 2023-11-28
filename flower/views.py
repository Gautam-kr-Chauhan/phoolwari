from django.shortcuts import render,redirect
from flower.models import Flower,Category
# Create your views here.

def all_flowers(request):
    flowers = Flower.objects.all()
    categories = Category.objects.all().order_by('category')
    # print(flowers.query)
    context = {
        "flowers" : flowers,
        "categories" : categories,
    }
    print(categories)
    return render(request, "page/all_flowers.html", context)

def flower_category(request,cid):
    flowers=Flower.objects.filter(category=cid)
    categories=Category.objects.all().order_by('category')
    # print(flowers.query)
    context={
        "flowers":flowers,
        "categories":categories
    }
    #print(categories)
    
    return render(request,"page/all_flowers.html",context)
