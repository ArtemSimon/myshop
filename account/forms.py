from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class OTPVerificationForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True,label="enter code")

class ConnectAuth(forms.Form):
    connect_auht = forms.ChoiceField(required=True,
                                    choices=([True,"Yes"], [False,'No']),
                                    widget=forms.RadioSelect,
                                    label='Выберете нужна ли вам двухфакторная аутентификация')

    