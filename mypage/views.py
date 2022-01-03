from django.shortcuts import render
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def index(request):
    context= {}
    return render(request, 'mypage/index.html')

def software(request):
    
    context={}
    return render(request, 'mypage/software.html')

def projects(request):
    context={}
    return render(request, 'mypage/projects.html')

def blogs(request):
    context={}
    return render(request, 'mypage/blogs.html')

def contact(request):
    form = contactForm()
    if request.method == 'POST':
        form = contactForm(request.POST)
        # validate form
        if form.is_valid():
            subject = "website inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_email(subject, message, 'dennismurage97@gmail.com', ['dennismurage97@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('mypage:index')

    context={'form': form}
    return render(request, 'mypage/contact.html', context)