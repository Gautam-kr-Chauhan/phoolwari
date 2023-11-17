from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello world,welcome to phoolwari")

def index(request):
    return render(request,'page/index.html')

def about(request):
    return render(request,'page/about2.html')




