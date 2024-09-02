"""
URL configuration for home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('index',views.index),
    path('ii',views.tryi),
    path('log',views.login),
    path('emplog',views.emplogin),
    path('empprof',views.empprofile),
    path('reg',views.u_register),
    path('con',views.contact),
    path('about',views.about),
    path('services',views.service),
    path('adminhom',views.adminhome),
    path('workerhom',views.workerhome),
    path('book',views.book),
    path('userhom',views.userhom),
    path('userabout',views.userabout),
    # path('userservices',views.userservices),
    path('usercon',views.usercontact),
    path('addservic',views.addservice),
    path('add',views.admin_add_products),
    path('viewuser',views.viewuser2),
    path('empregister',views.e_register),
    path('empview',views.viewepmloyee),
    path('viewservic',views.viewservice),
    path('userservices',views.user_service),
    path('edit_services/<int:id>',views.edit_service),
    path('edit/<int:id>',views.edit),
    path('delete/<int:id>',views.delete),
    path('ffeedback',views.ffeedback),
    path('feed',views.user_feedback),
    path('adminfeed',views.adminfeedback),
    path('adminorder',views.a_vieworder),
    # path('viewfeed',views.viewfeedback),
    path('usrprof',views.usr_profile),
    path('my_profile', views.usr_profile),
    path('user_profile_update/<int:id>', views.pro_edit, name='user_profile_update'),
    path('user_profile_update/<int:id>', views.update_profile),

    #forgot password>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    path('forgot',views.forgot_password,name="forgot"),
    path('reset/<token>',views.reset_password,name='reset_password'),
    #booking>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    path('booking/<int:id>/',views.bookingservice),

    #payment>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # path('payment/<int:price>/<int:pk>',views.payment),
    path('u_show',views.u_booking),
    path('u_book',views.u_bookreq),
    path('book_cancel/<int:id>/<int:pk>',views.book_cancel),
    #
    path('single_razor/<int:id>',views.single_razor,name='single_razor'),
    # path('razor',views.razor),
    path('razor_pay/<int:price>/<int:pk>',views.razorpaycheck),
    # path('success', views.success, name='success'),
    path('success/<int:id>/', views.success, name='success'),
    path('statusup/<int:booking_id>',views.statusup),
    path('u_bookreq_cancel/<int:id>',views.u_bookreq_cancel),
    path('ad_bookdt',views.adminbookingdetails),
    path('user_bookdt',views.userbookingdetails),


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)