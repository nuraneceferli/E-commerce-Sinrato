from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,'index.html')

def contactus(request):
    return render(request,'contact-us.html')


def about(request):
    return render(request,'about.html')

