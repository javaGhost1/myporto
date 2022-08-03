
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError, get_connection
from .forms import *
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



def contact(request):
    form = contactForm()
    if request.method == 'POST':
        form = contactForm(request.POST)
        # validate form
        if form.is_valid():
            subject = "Website inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, body['email'], ['dennismurage97@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('mypage:index')

    context={'form': form}
    return render(request, 'mypage/contact.html', context)