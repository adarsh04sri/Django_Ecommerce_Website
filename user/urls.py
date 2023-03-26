
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    path('mensproduct/',views.mensproduct),
    path('womensproduct/',views.wproduct),
    path('contact1/',views.contactus),
    path('kidsproduct/',views.kproduct),
    path('orders/',views.myorders),
    path('profile/',views.myprofile),
    path('viewproduct/',views.viewproduct),

]