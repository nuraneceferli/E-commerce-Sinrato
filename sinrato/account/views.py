from django.shortcuts import render

# Create your views here.



def myaccount(request):
    return render(request,'my-account.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')