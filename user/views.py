from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    mproduct=product.objects.all()[:8]
    return  render(request,'user/index.html',{"mixproduct":mproduct})
def mensproduct(request):
    a=request.GET.get('msg')
    if a==None:
        pdata=product.objects.filter(category='Mens')
    else:
        pdata=product.objects.filter(category='Mens',subcategory=a)

    scat=subcategory.objects.all().order_by('-id')
    my_dict={"data":pdata,"subcat":scat}
    return  render(request,'user/mensproduct.html',my_dict)
def wproduct(request):
    scat = subcategory.objects.all().order_by('-id')
    pdata = product.objects.filter(category='Womens')
    my_dict = {"data": pdata,"subcat":scat}
    return render(request,'user/wproduct.html',context=my_dict)
def contactus(request):
    status=False
    if request.method=="POST":
        Name=request.POST.get("a", "")
        Mobile=request.POST.get("mobno","")
        Msg=request.POST.get("msg","")
        Email=request.POST.get("email","")
        res=contactinfo(name=Name,email=Email,msg=Msg,mobno=Mobile)
        res.save()
        status=True

    return render(request,'user/contact.html',context={"S":status})
def kproduct(request):
    pdata = product.objects.filter(category='Kids')
    my_dict = {"data": pdata}
    return render(request,'user/kproduct.html',my_dict)

def myorders(req):
    return  render(req,'user/myorders.html')

def myprofile(request):
    return render(request,'user/myprofile.html')

def viewproduct(request):
    return render(request,'user/viewproduct.html')
