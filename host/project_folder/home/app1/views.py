from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from django.contrib import messages
from .forms import *
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
import re

def home(re):
    return render(re,'index.html')
def tryi(re):
    return render(re,'try.html')
def index(re):
    return render(re,'index.html')

def log(re):
    return render(re,'login.html')
def reg(re):
    return render(re,'register.html')
def contact(re):
    return render(re,'contact.html')
def about(re):
    return render(re,'about.html')
def service(re):
    return render(re,'services.html')
def adminhome(re):
    return render(re,'adminhome.html')
def workerhome(re):
    return render(re,'workerhome.html')
def book(re):
    return render(re,'book.html')
def userhom(re):
    return render(re,'userhom.html')
def userabout(re):
    return render(re,'userabout.html')
def userservices(re):
    return render(re,'userservices.html')
def usercontact(re):
    return render(re,'usercontact.html')
def addservice(re):
    return render(re,'addservice.html')
def viewuser(re):
    return render(re,'viewuser.html')
def empprofile(re):
    return render(re,'empprofile.html')
def empregister(re):
    return render(re,'empregister.html')
def emplogin(re):
    return render(re,'emplogin.html')
def customerfeed(re):
    return render(re,'customerfeedback.html')
def userprofile(re):
    return render(re, 'userprofile.html')


from .models import *
def u_register(request):
    if request.method=='POST':
        u_name=request.POST['name']
        uname= request.POST['username']
        email=request.POST['email']
        uadrs=request.POST['address']
        pncd=request.POST['pin']
        uphno=request.POST['phone']
        pwd=request.POST['password']
        u_image=request.POST['dimg']
        if len(pwd) < 8:
            messages.error(request, "Password must be at least 8 characters long")
            return render(request, 'register.html')

        special_char_pattern = r'[!@#$%^&*()_+=\-[\]{};:\'"\\|,.<>/?]'
        alph_pattern = r'[A-Za-z]'
        number_pattern = r'[0-9]'

        if not re.search(special_char_pattern, pwd):
            messages.error(request, "Password must contain at least one special character")
            return render(request, 'register.html')

        if not re.search(alph_pattern, pwd):
            messages.error(request, "Password must contain at least one uppercase letter")
            return render(request, 'register.html')

        if not re.search(number_pattern, pwd):
            messages.error(request, "Password must contain at least one number")
            return render(request, 'register.html')
        try:
            u=register.objects.get(username=uname)
            if u is not None:
                messages.error(request,'Username Already Exits')
                return render(request,'register.html')
        except register.DoesNotExist:
            try:
                u=register.objects.create(name=u_name,email=email,address=uadrs,pincode=pncd,phone=uphno,username=uname,password=pwd,img=u_image)
                u.save()
                messages.success(request, "Your Profile Details added Successfully")
            except IntegrityError:
                messages.error(request, 'Email already exists')
                return render(request, 'register.html')
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        try:
            new_user=register.objects.get(username=u)
            if u==new_user.username and p==new_user.password:
                request.session['id']=u
                return redirect(userhom)

            else:
                messages.error(request,'Invalid  password')
        except:
            try:
                new_user=empregister.objects.get(username=u)
                if u==new_user.username and p==new_user.password:
                    request.session['eid']=u
                    return redirect(workerhome)
                else:
                    messages.error(request, 'User not found')
            except Exception:
                if u=='admin' and p=='admin':
                    request.session['aid']=u
                    return redirect(adminhome)
                else:
                    messages.error(request,'User not found')
    return render(request,'login.html')

def admin_add_products(request): # to add new products
    if request.method=='POST':
        servicenam=request.POST['servicenam']
        description=request.POST['description']
        price=request.POST['price']
        image=request.FILES['image']
        data=services.objects.create(servicename=servicenam, description= description, price=price,image=image)
        data.save()
        messages.success(request," Added Successfully")
    return render(request,'addservice.html')

def viewuser2(re):
    if 'aid' in re.session:
        data=register.objects.all()
        return render(re,'viewuser.html', {'d':data})
    return redirect(adminhome)

def viewepmloyee(re):
    if 'aid' in re.session:
        data=empregister.objects.all()
        return render(re,'employeeview.html', {'d':data})
    return redirect(adminhome)

def e_register(request):
    if request.method=='POST':
        e_name=request.POST['name']
        ename= request.POST['username']
        email=request.POST['email']
        eadrs=request.POST['address']
        pncd=request.POST['pin']
        ephno=request.POST['phone']
        pwd=request.POST['password']
        id_proof=request.FILES['image']
        try:
            e=empregister.objects.get(username=ename)
            if e is not None:
                messages.error(request,'Username Already Exits')
        except Exception:
            e=empregister(name=e_name,email=email,address=eadrs,pincode=pncd,phone=ephno,username=ename,password=pwd,image=id_proof)
            e.save()
            messages.success(request, "Your Profile Details added Successfully")
    return render(request,'empregister.html')

def viewservice(re):
    if 'aid' in re.session:
        data=services.objects.all()
        return render(re,'viewservice.html', {'d':data})
    return redirect(adminhome)

def user_service(re):
    if 'id' in re.session:
        data = services.objects.all()
        return render(re, 'userservices.html', {'d': data})
    return redirect(userhom)

def  edit(re,id):
    if 'aid' in re.session:
        data=services.objects.get(pk=id)
        return render(re,'editservice.html',{'d':data})
def edit_service(re, id):
    if 'aid' in re.session:
        if re.method == 'POST':
            price = re.POST['s_price']
            description = re.POST['sdescription']
            sname= re.POST['s_name']
            # s_img = re.FILES['cs_img']
            services.objects.filter(pk=id).update(servicename=sname, description=description, price=price)
            return redirect(viewservice)
        return render(re, 'editservice.html')
def delete(re,id):
    if 'aid' in re.session:
        data=services.objects.get(pk=id)
        data.delete()
        messages.success(re,'services Deleted')
        return redirect(viewservice)

def adminfeedback(re):
    if 'aid' in re.session:
        data = feedback.objects.all()
        return render(re, 'adminfeedback.html', {'d': data})
    return redirect(adminhome)
def ffeedback(re):
    data = feedback.objects.all()

    return render(re, 'ffeedback.html',{'d': data})


def user_feedback(re):
    if 'id' in re.session:
        if re.method=='POST':
            name = re.POST['fname']
            femail = re.POST['femail']
            fmsg= re.POST['fmessage']
            fdbk = feedback.objects.create(name=name,email=femail,message=fmsg)
            fdbk.save()
            messages.success(re,'...Feedback Submitted Successfully...')
        return render(re, 'customerfeedback.html')
    return redirect(userhom)


def usr_profile(re):
    if 'id' in re.session:
        u = register.objects.get(username=re.session['id'])
        return render(re,'userprofile.html',{'d':u})
    return redirect(userhom)
def pro_edit(re,id):
    if 'id' in re.session:
        u = register.objects.get(pk=id)
        if re.method == 'POST':
            u.name = re.POST['name']
            u.email = re.POST['email']
            u.phone = re.POST['nmbr']
            u.address = re.POST['adrss']
            u.upincode  = re.POST['pincode']
            try:
                u.img = re.FILES['user_img']
                import os
                os.remove()
                u.save()
            except:
                u.save()
                return redirect(update_profile,id)
        return render(re,'userprofile.html',{'d':u})
    return redirect(userhom)


def update_profile(re,id):
    if 'id' in re.session:
        if re.method == 'POST':
            form=UserProfileForm(re.POST,re.FILES)
            if form.is_valid():
                a = form.cleaned_data['name']
                b = form.cleaned_data['email']
                c = form.cleaned_data['nmbr']
                d = form.cleaned_data['adrss']
                e = form.cleaned_data['user_img']
                f= form.cleaned_data['pincode ']
                register.objects.filter(pk=id).update(name=a,email=b,phone=c,address=d,img=e,pincode=f)
                messages.success(re,'...Profile Updated Successfully...')
                return redirect(usr_profile)
            data = register.objects.all()
            return render(re,'userprofile.html',{'d':data})
        form=UserProfileForm()
        return render(re,'userprofile.html',{'form':form})
    return redirect(usr_profile)

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = register.objects.get(email=email)
        except:
            messages.info(request,"Email id not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user=user, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            # return render(request, 'emailsent.html')
        except:
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'frgt.html')

def reset_password(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    # usr = User.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            password_reset.user.password=new_password
            password_reset.user.save()
            # password_reset.delete()
            return redirect(login)
    return render(request, 'rest-pass.html',{'token':token})
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def bookingservice(re, id):
        if 'id' in re.session:
            user = register.objects.get(username=re.session['id'])
            item = services.objects.get(pk=id)
            return render(re, 'book.html', {'user': user, 'd': item})
        # return redirect(userhom)


# def payment(request, price,pk):
#     if 'id' in request.session:
#             u = register.objects.get(username=request.session['id'])
#             s = Booking.objects.filter(name=u)
#             t = int(price) * 100
#             return render(request, "payment.html", {'amount': t,'pk':pk})
        # return render(request, "payment.html")


def u_bookreq(re):
    if 'id' in re.session:
        u = register.objects.get(username=re.session['id'])
        data = Booking.objects.filter(user=u)
        return render(re, 'userbooking.html', {'da': data})
    return render(re, 'userbooking.html')
def u_booking(re):
    data = Booking.objects.all()
    return render(re, 'book.html', {'d': data})


def book_cancel(re, id):
    if 'id' in re.session:
        data = Booking.objects.get(pk=id)
        data.delete()
        return redirect(u_booking)


def single_razor(re,id):
    srvice=get_object_or_404(services,pk=id)
    user = get_object_or_404(register,username=re.session['id'])
    if re.method == "POST":
        name = re.POST['name']
        email = re.POST['Email']
        service_name = re.POST.get('Service')
        price = re.POST.get('Price')
        address = re.POST['Address']
        location = re.POST['Location']
        number = re.POST['Number']
        pin_code = re.POST['Pin']
        date=re.POST['date']
        print('date is',date)
        booking1 = Booking.objects.create(
            service=srvice,
            user=user,
            email=email,
            service_name=service_name,
            location=location,
            pincode=pin_code,
            ur_name=name,
            address=address,
            number=number,
            price=price,
            date=date,

        )

        booking1.save()
        messages.success(re,'booking request sended')
        # return redirect(razorpaycheck, services.price)
        return redirect(u_bookreq)
    #     return JsonResponse({'status': 'Your order has been placed successfully'})
    #
    return redirect(userhom)


# def razor(re):
#     return render(re, "payment.html")
def a_vieworder(re):
    data = Booking.objects.all()
    return render(re, 'adminvieworder.html',{'da':data})

# def u_dis_bookings(re):
#     if 'id' in re.session:
#         data=register.objects.get(username=re.session['id'])
#         u=booked.objects.filter(booked_name=data.user_name)
#         return render(re,'u_dis_bookings.html',{'d':u})
def razorpaycheck(request,price,pk):
    if 'id' in request.session:
        u = register.objects.get(username=request.session['id'])
        s=Booking.objects.filter(user=u)
        t = price * 100
        return render(request, "payment.html", {'amount': t,'pk':pk})
    return render(request, "payment.html")


def success(re,id):
    if 'id' in re.session:
        s = Booking.objects.get(pk=id)
        a = booked.objects.create(
                                  name=s.ur_name,
                                  email=s.email,
                                  address=s.address,
                                  number=s.number,
                                  s_name=s.service_name,
                                  s_price=s.price,
                                  pincode=s.pincode,
                                  date=s.date,
                                  payment_mode='Razor_pay')
        a.save()
        print(a)
        v=booked.objects.all()
        return render(re, 'success.html',{'c':v})
    return render(re,'success.html')

def conf_bookreq(request):
    if 'id' in request.session:
        data =register.objects.get(username=request.session['id'])
        u = Booking.objects.filter(servicename=data.username)
        return render(request, 'adminvieworder.html', {'da': u,'s':data})

def statusup(re, booking_id):
    if re.method == "POST":
        st = Booking.objects.get(id=booking_id)
        st.status = re.POST.get('status')
        st.save()
    return redirect(a_vieworder)

def u_bookreq_cancel(re,id):
    if 'id' in re.session:
        data = Booking.objects.get(pk=id)
        data.delete()
    return redirect(u_bookreq)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def adminbookingdetails(re):
    if 'id' in re.session:
        v=booked.objects.all()
        return render(re, 'adminviewbooked.html', {'c': v})
    return render(re, 'adminviewbooked.html')
def userbookingdetails(re):
    if 'id' in re.session:
        v=booked.objects.all()
        return render(re, 'userorder.html', {'c': v})
    return render(re, 'userorder.html')