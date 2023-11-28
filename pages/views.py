from django.shortcuts import render,HttpResponse
from flower.models import Category,Flower
# Create your views here.
def hello(request):
    return HttpResponse("Hello world,welcome to phoolwari")

def index(request):
    categories=Category.objects.all()
    return render(request,"page/index.html",{'categories':categories})

def about(request):
    return render(request,'page/about2.html')





