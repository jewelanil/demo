from django import forms
from .models import *

# Create your formss here.

class UserProfileForm(forms.Form):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)
    email = models.EmailField()
    img = models.FileField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    pincode = models.IntegerField()