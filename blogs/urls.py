from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path("blogs", views.blogs, name='blogs'),
    path('blog/<int:blog_id>/', views.blog, name='blog'),
    
]
