import hashlib
from dal.user_repository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def verify_credentials(self, username, password):
        user = self.user_repo.find_user(username)
        if not user:
            return False
        stored_password = user[2]  # password stored in DB
        return stored_password == hashlib.sha256(password.encode()).hexdigest()

    def send_otp(self, username):
        otp = str(hashlib.sha256(username.encode()).hexdigest())[:6]  # Simple OTP generation
        self.user_repo.update_otp(username, otp)
        print(f"OTP для {username}: {otp}")  # Here you can send OTP via SMS/email

    def verify_otp(self, username, otp):
        user = self.user_repo.find_user(username)
        if user and user[3] == otp:
            return True
        return False

    def register_user(self, username, password):
        # Перевіряємо, чи користувач вже існує
        existing_user = self.user_repo.find_user(username)
        if existing_user:
            return False, "Користувач з таким ім'ям вже існує."

        # Хешуємо пароль і зберігаємо його
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.user_repo.add_user(username, hashed_password)
        return True, "Користувач успішно зареєстрований!"
