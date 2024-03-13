from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User, auth
from requests import post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string

from .forms import EventForm

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

'''def Event(request):
    print(request.user)
    #event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html',) #{'event': event})'''

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')  # Redirect to the events page after successfully creating an event
    else:
        form = EventForm()
    return render(request, 'event_detail.html', {'form': form})

def register(request):
    pass

def events(request):
    print(request.user)
    
    return render(request, 'events.html', {'events': events})
def buy_events(request):
    print(request.user)
    
    return render(request, 'buyevents.html')


def generate_ticket_code(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def buy_tickets(request):
    
    
    
    return render(request, "buy_tickets.html")
