from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    role_id = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        related_name="users"
    )
    department_id = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
        related_name="users"
    )

    
class Department(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    #User.objects.get(pk=1)
    #User.objects.create(name="John Doe", email="john@example.com", number="1234567890")