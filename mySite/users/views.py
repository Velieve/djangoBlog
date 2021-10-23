from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm


# Create your views here.

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
                return redirect('/admin ')
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
            new_user.set_password(form.cleaned_data['password']) 
            new_user.save()
            return HttpResponse('Succesfull register') 
    context = {'form': form}
    return render(request,'users/register.html',context)
