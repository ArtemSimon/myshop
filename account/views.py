# Create your views here.

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.contrib.auth.views import LoginView

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()          # Сохраняем нового пользователя
            login(request, user)        # Выполняем вход
            return redirect('shop:product_list')     # Перенаправляем на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password) # Проверяем учетные данные
            if user is not None:
                # login(request, user)     # Выполняем вход
                request.session['auth_login'] = user
                return redirect('shop:product_list')  # Перенаправляем на главную страницу
    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    # return redirect('account:login')
    return render(request, 'account/logout.html')
