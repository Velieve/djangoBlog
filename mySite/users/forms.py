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
    username = forms.CharField(label='Username', min_length=8, widget=forms.TextInput(
        attrs={'class:': 'input', 'placeholder': 'Username/Email'}))
    password = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput(
        attrs={'class:': 'input', 'placeholder': 'Password'}))
    password1 = forms.CharField(label='Repeat your password', min_length=8, widget=forms.PasswordInput(
        attrs={'class:': 'input', 'placeholder': 'Repeat your assword'}))

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        exists = User.objects.filter(username=username).exists()
        if exists:
            raise forms.ValidationError('User already exists.')
        return username

    def clean_password(self):
        if self.cleaned_data.get('password')!= self.cleaned_data.get('password1'):
            raise forms.ValidationError('Error: Review your passwords.')
        return self.cleaned_data['password1']
