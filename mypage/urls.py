from django.urls import path, include
from . import views

app_name = "mypage"
urlpatterns = [
    path('', views.index, name='index'),
    path('software/', views.software, name='software'),
    path('projects/', views.projects, name='projects'),
    path('blogs/', views.blogs, name='blogs'),
    path('contact/', views.contact, name='contact'),
    
]
