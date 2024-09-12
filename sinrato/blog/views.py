from django.shortcuts import render

# Create your views here.
def blogs(request):
    return render(request, 'blog-right-sidebar-3.html')

def blog_detail(request):
    return render(request, 'blog-details.html')