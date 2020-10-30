from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form_control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form_control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={'class': 'form_control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs={'class': 'form_control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')