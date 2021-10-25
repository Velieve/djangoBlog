from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login

from .forms import ForgetPwdFrom, LoginForm, RegisterForm, ModifyPwdForm
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import EmailVerifyRecord, UserProfile
from utils.email_send import send_register_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.


class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None,):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def active_user(request, active_code):
    all_records = EmailVerifyRecord.objects.filter(code=active_code)
    if all_records:
        for record in all_records:
            email = record.email
            user = User.objects.get(email=email)
            user.is_staff = True
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
            if user is not None:
                login(request, user)
                return redirect('users:user_profile')
            else:
                return HttpResponse('Login failured')
    return render(request, 'users/login.html', {'form': form})


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
            send_register_email(form.cleaned_data['email'], 'register')
            return HttpResponse('Succesfull register')
    context = {'form': form}
    return render(request, 'users/register.html', context)


def forget_pwd(request):
    if request.method == 'GET':
        form = ForgetPwdFrom()
    elif request.method == 'POST':
        form = ForgetPwdFrom(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            exists = User.objects.filter(email=email).exists()
            if exists:
                send_register_email(email, 'forget')
                return HttpResponse('Please check your email inbox.')
            else:
                return HttpResponse('Email not registed.')
    context = {'form': form}
    return render(request, 'users/forget_pwd.html', context)

def forget_pwd_url(request,active_code):
    if request.method != 'POST':
        form = ModifyPwdForm()
    else:
        form = ModifyPwdForm(request.POST)
        if form.is_valid():
            record = EmailVerifyRecord.objects.get(code= active_code)
            email = record.email
            user = User.objects.get(email=email)
            user.username = email
            user.password = make_password(form.cleaned_data.get('password'))
            user.save()
            return HttpResponse('Correct change.')
        else:
            return HttpResponse('Failed change.')
    context = {'form': form}
    return render(request,'users/reset_pwd.html',context)

@login_required(login_url='users:login')
def user_profile(request):
    user = User.objects.get(username = request.user)
    context = {'user': user}
    render(request,'users/user_profile.html',context)