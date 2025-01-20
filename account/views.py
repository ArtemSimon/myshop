# Create your views here.

from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm, OTPVerificationForm,ConnectAuth
from django.contrib.auth.views import LoginView
from .utils import generate_otp, verify_otp
from django.core.mail import send_mail
from .models import UserOTP
from django.contrib import messages


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
            user = authenticate(request,username=username, password=password) # Проверяем учетные данные

            if user:
         

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
                    messages.error(request,'no valid code ')
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

@login_view
def connnect_auth(request):
    if request.method == 'POST':
        form = ConnectAuth(request.POST)
        user = User.objects.get(id=id)

        if form.is_valid():
            user_choise = form.cleaned_data['connect_auht']

            if user_choise:
                user_otp = UserOTP.objects.create(user)
                redirect('account:login')
            else:
                record = get_object_or_404(UserOTP,id)
                record.delete()
                redirect('account:login')
                
                

