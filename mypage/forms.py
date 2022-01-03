from django import forms
from .models import *

class contactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=False)
    email_address = forms.EmailField(max_length=150, required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=2000, required=True)
    # class meta:
    #     model = contact
    #     fields = ['text']
    #     labels = {'text': ''}

