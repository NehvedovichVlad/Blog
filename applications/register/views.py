from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import login, logout
from applications.register.forms import UserRegisterForm, UserLoginForm, ContactForm
from django.core.mail import send_mail

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Вы успешно зарегистрировались: {user}')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'register/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login') 


def contact_mail(request):
    """Необходима для формы обратной связи"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data[
                'content'], 'settings@mail.ru', ['another@mail.ru'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправленно')
                return redirect('contact')
        else:
            messages.error(request, 'Ошибка отправки')
    else:
        form = ContactForm()
    return render(request, 'register/register.html', {'form': form})

