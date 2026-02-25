from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import login
import boto3
import json
from django.shortcuts import render
from django.http import JsonResponse
from decouple import config

s3_client = boto3.client(
    's3',
    aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
    region_name=config('AWS_S3_REGION_NAME')
)
def upload_file(request):
    return render(request, 'upload.html')

def handle_upload(request):
    if request.method == 'POST' and request.FILES.get('my_file'):
        file_obj = request.FILES['my_file']
        bucket_name = config('AWS_STORAGE_BUCKET_NAME')

        # We define where in S3 the file goes
        # 'uploads/' is the folder, file_obj.name is the actual filename
        file_path = f"uploads/{file_obj.name}"

        try:
            s3_client.upload_fileobj(file_obj, 
                                     bucket_name, 
                                     file_path,
                                     ExtraArgs={'ContentType': file_obj.content_type})
            return JsonResponse({'message': 'File uploaded successfully', 'file': file_obj.name}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        return JsonResponse({'error': 'Invalid request'}, status=400)

def trigger_zip_repsonse(request):
    lambda_client = boto3.client(
        'lambda',
        aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
        region_name=config('AWS_S3_REGION_NAME')
    )    
    payload = {
        "bucket": config('AWS_STORAGE_BUCKET_NAME'),
        "folder_prefix": "uploads/" 
    }
    response = lambda_client.invoke(
        FunctionName='ZipMyFilesFunction',
        InvocationType='RequestResponse',
        Payload=json.dumps(payload)
    )
    result = json.loads(response['Payload'].read())
    return JsonResponse({'download_url': result.get('download_url')})

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
