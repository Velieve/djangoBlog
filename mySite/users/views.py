from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm, RegisterForm
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import EmailVerifyRecord
from utils.email_send import send_register_email

# Create your views here.

class MyBackend(ModelBackend):
    def authenticate(self, request, username=None,password=None,):
        try:
            user = User.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

def active_user(request,active_code):
    all_records=EmailVerifyRecord.objects.filter(code=active_code)
    if all_records:
        for record in all_records:
            email = record.email
            user = User.objects.get(email=email)
            user.is_staff=True
            user.save()

    else:
        return HttpResponse('Wrong link')

    return redirect('users:login')


def login_view(request):
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not  None:
                login(request,user)
                return redirect('/admin')
            else:
                return HttpResponse('Login failured')
    return render(request, 'users/login.html',{'form':form})

def register(request):
    if request.method != 'POST':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.username = form.cleaned_data.get('email')
            new_user.save()
            send_register_email(form.cleaned_data['email'],'register')
            return HttpResponse('Succesfull register') 
    context = {'form': form}
    return render(request,'users/register.html',context)
