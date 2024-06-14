from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main.models import Record
from .forms import LoginForm


def login_user(request):
    """Функция-представление авторизации пользователя."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('users:profile')
            else:
                return redirect('main:index')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context=context)


@login_required
def history(request):
    """Функция-представление истории записей."""
    user = request.user
    records = Record.objects.filter(employee=user)
    context = {'records': records}
    return render(request, 'users/history.html', context=context)


@login_required
def profile(request):
    """Функция-представление личного кабинета мастера."""
    context = {'user': request.user}
    return render(request, 'users/room.html', context=context)


@login_required
def logout_user(request):
    """Функция-представление выхода пользователя."""
    logout(request)
    return redirect('users:login')
