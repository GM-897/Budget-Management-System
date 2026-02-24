from django.contrib import admin
from .models import User

#what ever is added here we can see that in admin panel
admin.site.register(User)