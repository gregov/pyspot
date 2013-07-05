# Create your views here.
from django.shortcuts import render
from django import forms
from register.models import Clients


class LoginForm(forms.Form):
    email = forms.EmailField( label=u'Votre e-mail' )

def index(request):
    form = LoginForm(request.POST)
    context = { 'form' : form,
                'sent' : False
              }  
    
    return render(request,'register/index.html',context)


def validate(request,secret):
    context = {} 
    return render(request,'register/validate.html',context)

