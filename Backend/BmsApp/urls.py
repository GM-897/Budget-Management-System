from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('budget/', views.budget, name='budget'),
    path('expenses/', views.expenses, name='expenses'),
    path('department/', views.department, name='department'),
    path('upload-page/', views.upload_file, name='upload_page'),
    path('upload/', views.handle_upload, name='handle_upload'),
    path('trigger-zip/', views.trigger_zip_repsonse, name='trigger_zip_process'),
]