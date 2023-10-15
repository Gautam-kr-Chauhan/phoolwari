from django.shortcuts import render,redirect

# Create your views here.
def all_flowers(request):
    return render(request,'page/all_flowers.html')