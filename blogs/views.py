from django.shortcuts import render
from .models import *

# Create your views here.
def blogs(request):
    # contains what to display on blogs page
    blogs = Blog.objects.order_by('date_added')
    # entries = Entry.objects.order_by('topic')?
    context = {'blogs': blogs}
    return render(request, 'mypage/blogs.html', context)

def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, 'mypage/blog.html', context)