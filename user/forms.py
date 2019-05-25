from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
 
 
class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Username:', min_length=4, max_length=150)
    
    first_name = forms.CharField(label='Tên', min_length=0, max_length=150)
    last_name = forms.CharField(label='Họ', min_length=0, max_length=150)
    email = forms.EmailField(label='Nhập email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput)
 
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username đã tồn tại")
        return username
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email đã tồn tại")
        return email
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Mật khẩu không khớp")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            username = self.cleaned_data['username'],
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password1'],
            last_name = self.cleaned_data['last_name'],
            first_name = self.cleaned_data['first_name'],
        )
        return user