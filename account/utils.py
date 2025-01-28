import pyotp


 # генерирует код на основе секретного ключа 
def generate_otp(self):
    totp = pyotp.TOTP(self.otp_secret)
    return totp.now()

# проверяет его корректность ввода 
def verify_otp(self,otp):
    totp = pyotp.TOTP(self.otp_secret)
    return totp.verify(otp)


def create_secret(self):
    self.otp_secret = pyotp.random_base32()
    return self.otp_secret