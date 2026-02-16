from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def budget(request):
    return render(request, 'budget.html')

def expenses(request):
    return render(request, 'expense.html')

def department(request):
    return render(request, 'department.html')
