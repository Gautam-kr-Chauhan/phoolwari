from django.shortcuts import render,redirect
from django.contrib.auth.models import User # User Model
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# from .models import Flower 

# Create your views here.
def signup(request):
    
    if request.method == "POST":
        messages.error(request, "")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # print(first_name, last_name, username, email, password)
        user_exists = False
        if User.objects.filter(username=username).exists():
            # print("username is already taken")
            messages.error(request, "Username is already taken. try with a new username")
            user_exists = True
        else:
            messages.error(request, "")
        
        if User.objects.filter(email=email).exists():
            # print("Email is already taken")
            messages.error(request, "Email is already taken. try with a new one")
            user_exists = True
        else:
            messages.error(request, "")

        if user_exists:
            return render(request, 'user/signup.html')
        
        user = User.objects.create_user(
           first_name=first_name, 
           last_name=last_name, 
           email=email, 
           username=username, 
           password=password
        )
        user.save()
        messages.success(request, "Account Created Successfully. Login to Continue")

    return render(request, 'user/signup.html')

def signin(request):
    # if request.user.is_authenticated:
    #     return render(request,'page/all_flowers.html')
    if request.method== "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Username or password")
            return render(request,'user/signin.html')
        else:
            login(request,user)
            return redirect('index')
    return render(request,'user/signin.html')
@login_required(login_url='/user/signin')
def signout(request):
    logout(request)
    return render(request, 'user/signin.html')

# def add_flowers(request):
#     if request.method=='POST':
#         type=request.POST.get('type')
#         name=request.POST.get('name')
#         quantity=request.POST.get('quantity')
#         flower=Flower(
#          user=request.user,
#          type=type,
#          name=name,
#          quantity=quantity   
#         )
#         print(flower.name,flower.type,flower.quantity)
#         flower.save()
#     return redirect('index')