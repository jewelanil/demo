from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100, default='default_password')
    email = models.EmailField(unique=True)
    img = models.FileField()
    phone = models.IntegerField(default=1234567890)
    address = models.CharField(max_length=200)
    pincode = models.IntegerField(default=123456)


class services(models.Model):
    servicename=models.CharField(max_length=200)
    description=models.TextField(max_length=300)
    price=models.IntegerField()
    image=models.FileField()

class empregister(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100, default='default_password')
    email = models.EmailField(unique=True)
    phone = models.IntegerField(default=1234567890)
    address = models.CharField(max_length=200)
    pincode = models.IntegerField(default=123456)
    image = models.FileField()

class feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.CharField(max_length=200)

class PasswordReset(models.Model):
    user=models.ForeignKey(register,on_delete=models.CASCADE)
    #security
    token=models.CharField(max_length=4)

class Booking(models.Model):
    user = models.ForeignKey(register,on_delete=models.CASCADE)
    service = models.ForeignKey(services,on_delete=models.CASCADE)
    ur_name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    service_name=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=200,null=True)
    price=models.IntegerField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=True)
    pincode=models.IntegerField(max_length=200,null=True)
    number=models.IntegerField(max_length=50,null=True)
    date=models.CharField(max_length=50,null=True)
    orderstatus=(
        ('Accepted','Accepted'),
        ('Finished','Finished'),
        ('pending','pending'),
        ('cancelled','cancelled')
    )
    status=models.CharField(max_length=150,choices=orderstatus,default='pending',null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

class booked(models.Model):
    # booking_id = models.IntegerField(unique=True)
    name= models.CharField(max_length=500)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=500)
    number = models.IntegerField()
    pincode = models.IntegerField(null=True)
    date=models.CharField(max_length=50,null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    s_name = models.CharField(max_length=200, null=True)
    s_price = models.IntegerField(null=True)
    payment_mode = models.CharField(max_length=200, default='Razor_pay', null=True)