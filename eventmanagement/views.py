from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from requests import post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        email = request.POST.get['email']
        password = request.POST.get['password']
        password2 = request.POST.get['password2']
        
        
        if len(password) < 8:
            messages.error(request, 'Password must be above eight charachters')
            return redirect('signup')
            
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already taken.')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signup')       
        
        if password != password2:
            messages.error(request, 'Passwords do not Match.') 
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect('signup')   
            
            myuser = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account Created Successfully")
            return redirect('login')
        
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  

    return render(request, 'login.html')



def home(request):
    print(request.user)
    return render(request, 'index.html')



        
        