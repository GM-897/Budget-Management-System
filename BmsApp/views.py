from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    return Response({
        "message": "Welcome to Dashboard, Yahooo 🚀",
        "user": request.user.username
    })

def home(request):
    return render(request, 'home.html')

def budget(request):
    return render(request, 'budget.html')

def expenses(request):
    return render(request, 'expense.html')

def department(request):
    return render(request, 'department.html')
