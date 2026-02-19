from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('budget/',views.budget, name='budget'),
    path('expenses/', views.expenses, name='expenses'),
    
]