import pyotp

class OTPService:
    def generate_secret(self):
        return pyotp.random_base32()

    def generate_otp(self, secret):
        totp = pyotp.TOTP(secret)
        return totp.now()

    def validate_otp(self, secret, input_otp):
        totp = pyotp.TOTP(secret)
        return totp.verify(input_otp)

# Приклад використання
otp_service = OTPService()

# Генерація нового секретного ключа для кожної сесії користувача
secret = otp_service.generate_secret()
generated_otp = otp_service.generate_otp(secret)
print(f"Згенерований OTP: {generated_otp}")

# Валідація OTP
input_otp = input("Введіть OTP: ")
if otp_service.validate_otp(secret, input_otp):
    print("OTP вірний!")
else:
    print("OTP невірний!")
