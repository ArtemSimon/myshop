from django.db import models
from django.contrib.auth.models import User,AbstractUser
import pyotp
from django.utils import timezone

class UserOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp_secret = models.CharField(max_length=32,blank=True)
    last_login = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username
    
    # генерирует код на основе секретного ключа 
    def generate_otp(self) -> int:
        totp = pyotp.TOTP(self.otp_secret)
        return totp.now()

    # проверяет его корректность ввода 
    def verify_otp(self,otp) -> bool:
        totp = pyotp.TOTP(self.otp_secret)
        return totp.verify(otp)
  
    # def create_secret(self):
    #     self.otp_secret = pyotp.random_base32()
    #     return self.otp_secret