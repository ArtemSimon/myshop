from django.urls import path
from account.views import signup_view, login_view,logout_view,verify_otp_view
from django.contrib.auth.views import LogoutView

app_name = 'account'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('otp_verify/',verify_otp_view, name='otp_verify' )
]