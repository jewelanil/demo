from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(register)
admin.site.register(services)
admin.site.register(empregister)
admin.site.register(feedback)
admin.site.register(Booking)
admin.site.register(booked )