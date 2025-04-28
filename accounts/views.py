from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.models import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            identifier = request.POST.get('username')
            password = request.POST.get('password')

        
            if '@' in identifier:
                user_obj = User.objects.get(email=identifier)
                username = user_obj.username
            else:
                username = identifier

            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.add_message(request, messages.SUCCESS, 'your logged in successfully')
                login(request, user)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'something went wrong')
                return redirect('/')

        return render(request, 'accounts/login.html')
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            
            if password1 != password2:
                messages.error(request, 'Passwords do not match.')
                return redirect('/')
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('/')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.')
                return redirect('/')

            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()

            messages.success(request, 'You signed up successfully.')
            return redirect('/')
            
        
        return render(request, 'accounts/signup.html')
    else:
        return redirect('/')


