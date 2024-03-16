from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User, auth
from requests import post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import stripe
from django.urls import reverse
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

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
        authenticate(username=username,password=password)
 
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
    return render(request, 'base.html')

def events(request):
    print(request.user)
    return render(request, 'events.html', {'events': events})

def buy_events(request):
    print(request.user)
    return render(request, 'buyevents.html')

def buy_tickets(request):
    return render(request, 'buy_tickets.html')

def credit_card(request):
    print(request.user)
    return render(request, 'credit_card.html')

def charge(request):
    
    amount = 5 
    if request.method == 'POST':
        print('Data', request.POST)
        
        stripe.Customer.create(
            email = request.POST.get('email'),
            name = request.POST.get('name'),
        )
        
        return redirect(reverse('success', args=[amount]))
    
def successMsg(request, args):
    amount = args
    return render(request, 'base.success.html', {'amount':amount})

