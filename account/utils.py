import pyotp


 # генерирует код на основе секретного ключа 
def generate_otp(self):
    totp = pyotp.TOTP(self.otp_secret)
    return totp.now()

# проверяет его корректность ввода 
def verify_otp(self,otp):
    totp = pyotp.TOTP(self.otp_secret)
    return totp.verify(otp)
   