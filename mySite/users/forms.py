from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32, widget=forms.TextInput(
        attrs={'class:': 'input', 'placeholder': 'Username/Email'}))
    password = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput(
        attrs={'class:': 'input', 'placeholder': 'Password'}))

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username == password:
            raise forms.ValidationError('Username cant be == Password')
        return password


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email', min_length=8, widget=forms.EmailInput(
        attrs={'class:': 'input', 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput(
        attrs={'class:': 'input', 'placeholder': 'Password'}))
    password1 = forms.CharField(label='Repeat your password', min_length=8, widget=forms.PasswordInput(
        attrs={'class:': 'input', 'placeholder': 'Repeat your assword'}))

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('Email already exists.')
        return email

    def clean_password1(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError('两次密码输入不一致！')
        return self.cleaned_data['password1']