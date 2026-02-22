from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login

@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            request.session['access_token'] = str(refresh.access_token)
            request.session['refresh_token'] = str(refresh)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')    
    return render (request, 'dashboard.html', {'user': request.user})

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home.html', {'user': request.user})

def budget(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'budget.html', {'user': request.user})

def expenses(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'expense.html', {'user': request.user})

def department(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'department.html', {'user': request.user})
