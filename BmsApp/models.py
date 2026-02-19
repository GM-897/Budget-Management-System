from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    email= models.EmailField(unique=True)
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

    #User.objects.get(pk=1)
    #User.objects.create(name="John Doe", email="john@example.com", number="1234567890")