from django.shortcuts import render

# Create your views here.


def product(request):
    return render(request,'product-details.html')

def shop(request):
    return render(request,'shop-grid-left-sidebar-4-column.html')