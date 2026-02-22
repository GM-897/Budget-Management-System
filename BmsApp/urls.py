from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('budget/', views.budget, name='budget'),
    path('expenses/', views.expenses, name='expenses'),
    path('department/', views.department, name='department'),
]