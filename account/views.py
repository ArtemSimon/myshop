# Create your views here.

from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
import pyotp
from django.views.decorators.http import require_POST
from .forms import SignUpForm, LoginForm, OTPVerificationForm,ConnectAuth
from django.contrib.auth.views import LoginView
from .utils import generate_otp, verify_otp,create_secret
from django.core.mail import send_mail
from .models import UserOTP
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password) # Проверяем учетные данные

            if user:
         
                try:
                    user_otp = UserOTP.objects.get(user=user)
                    otp = user_otp.generate_otp()
                    send_mail(
                    'Your otp code', 
                    f'Your otp code is {otp}',
                    'artemsim2006@mail.ru',
                    [user.email],
                    )
                    request.session['user_id'] = user.id 
                    return redirect('account:otp_verify')
            
                except UserOTP.DoesNotExist:
                   login(request,user)
                   return redirect('shop:product_list')



    else:
        form = LoginForm()        
    return render(request, 'account/login.html', {'form': form})


def verify_otp_view(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect('account:login')
    try:
        user = User.objects.get(id=user_id)
        user_otp = UserOTP.objects.get(user=user)
    

        if request.method == 'POST':
            form = OTPVerificationForm(request.POST)
            if form.is_valid():
                otp = form.cleaned_data['otp']
                if user_otp.verify_otp(otp):
                    del request.session['user_id']
                    login(request, user)
                    return redirect('shop:product_list')
                else: 
                    messages.error(request,'Error: no valid code ')
                    return render(request, 'account/otp_verify.html', {'form': form, "error": 'invalid OTP'})
        else:
            form = OTPVerificationForm()
        return render (request,'account/otp_verify.html',{'form': form})
    
    except UserOTP.DoesNotExist:
        messages.error(request, "пользователь не настроил двучфакторную аутентификацию")
        return redirect('account:login')

def logout_view(request):
    logout(request)
    return render(request, 'account/logout.html')

@login_required
def connnect_auth_view(request):
    if request.method == 'POST':

        form = ConnectAuth(request.POST)

        if form.is_valid():
            user_choise = form.cleaned_data['connect_auth']
            user = request.user
            
            secret = pyotp.random_base32()

            print(f"User: {user}, Choice: {user_choise}, Secret: {secret}")  # Отладочная информация

            if user_choise == 'True':
                user_otp,created = UserOTP.objects.get_or_create(user=user,
                                                    defaults={'otp_secret':secret})
                
                print(f"UserOTP created: {created}")  # Отладочная информация

                if not created:
                    return redirect('shop:product_list')
                else:
                    return redirect('shop:product_list')

            if user_choise == 'False':

                if UserOTP.objects.filter(user=user).exists():
                    record = get_object_or_404(UserOTP,user=user)
                    record.delete()
                    print("UserOTP deleted")  # Отладочная информация
                return redirect('account:login')
    else:
        form = ConnectAuth()     
    return render(request,'account/create_2auth.html', {'form':form})

