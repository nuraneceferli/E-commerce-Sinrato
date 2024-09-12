from django.urls import path
from . import views

urlpatterns=[
    path('blogs/',views.blogs, name='blogs'),
    path('blog_detail/',views.blog_detail,name='blog_detail')
 
]