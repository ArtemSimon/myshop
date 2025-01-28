from django.urls import path
from account.views import signup_view, login_view,logout_view,verify_otp_view,connnect_auth_view
from django.contrib.auth.views import LogoutView

app_name = 'account'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('otp_verify/',verify_otp_view, name='otp_verify'), 
    path('two_auth_setting/',connnect_auth_view, name='connect_auth'),

]