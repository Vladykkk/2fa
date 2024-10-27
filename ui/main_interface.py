import tkinter as tk
from tkinter import messagebox
from tkinter import font
from bll.auth_service import AuthService

class MainInterface:
    def __init__(self, root):
        self.auth_service = AuthService()
        self.root = root
        self.root.title("Двофакторна Автентифікація")

        # Налаштування розмірів вікна
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Налаштування глобальних шрифтів
        self.title_font = font.Font(family="Arial", size=18, weight="bold")
        self.label_font = font.Font(family="Arial", size=12)
        self.button_font = font.Font(family="Arial", size=10)

        # Головне меню
        self.create_main_menu()

    def create_main_menu(self):
        # Очищення всіх попередніх віджетів
        for widget in self.root.winfo_children():
            widget.destroy()

        # Відступи
        pady = 15
        padx = 10

        # Титульний текст
        tk.Label(self.root, text="Двофакторна Автентифікація", font=self.title_font).pack(pady=(20, 10))

        # Кнопки з відступами та шрифтами
        tk.Button(self.root, text="Реєстрація", font=self.button_font, command=self.register, width=20, height=2).pack(pady=pady)
        tk.Button(self.root, text="Вхід", font=self.button_font, command=self.login, width=20, height=2).pack(pady=pady)
        tk.Button(self.root, text="Вихід", font=self.button_font, command=self.root.quit, width=20, height=2).pack(pady=pady)

    def register(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        pady = 10
        padx = 10

        # Реєстрація - заголовок
        tk.Label(self.root, text="Реєстрація", font=self.title_font).pack(pady=(20, 10))

        # Поля для вводу
        tk.Label(self.root, text="Ім'я користувача:", font=self.label_font).pack(pady=pady)
        username_entry = tk.Entry(self.root, font=self.label_font)
        username_entry.pack(pady=pady, padx=padx)

        tk.Label(self.root, text="Пароль:", font=self.label_font).pack(pady=pady)
        password_entry = tk.Entry(self.root, font=self.label_font, show="*")
        password_entry.pack(pady=pady, padx=padx)

        def submit_registration():
            username = username_entry.get()
            password = password_entry.get()
            success, message = self.auth_service.register_user(username, password)
            if success:
                messagebox.showinfo("Успішно", "Користувач успішно зареєстрований!")
                self.create_main_menu()
            else:
                messagebox.showerror("Помилка", message)

        # Кнопки з відступами
        tk.Button(self.root, text="Зареєструватися", font=self.button_font, command=submit_registration, width=15, height=2).pack(pady=(20, pady))
        tk.Button(self.root, text="Назад", font=self.button_font, command=self.create_main_menu, width=15, height=2).pack(pady=pady)

    def login(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        pady = 10
        padx = 10

        tk.Label(self.root, text="Вхід", font=self.title_font).pack(pady=(20, 10))

        tk.Label(self.root, text="Ім'я користувача:", font=self.label_font).pack(pady=pady)
        username_entry = tk.Entry(self.root, font=self.label_font)
        username_entry.pack(pady=pady, padx=padx)

        tk.Label(self.root, text="Пароль:", font=self.label_font).pack(pady=pady)
        password_entry = tk.Entry(self.root, font=self.label_font, show="*")
        password_entry.pack(pady=pady, padx=padx)

        def submit_login():
            username = username_entry.get()
            password = password_entry.get()
            if self.auth_service.verify_credentials(username, password):
                self.send_otp(username)
            else:
                messagebox.showerror("Помилка", "Невірне ім'я користувача або пароль.")

        tk.Button(self.root, text="Увійти", font=self.button_font, command=submit_login, width=15, height=2).pack(pady=(20, pady))
        tk.Button(self.root, text="Назад", font=self.button_font, command=self.create_main_menu, width=15, height=2).pack(pady=pady)

    def send_otp(self, username):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.auth_service.send_otp(username)

        pady = 10
        padx = 10

        tk.Label(self.root, text="Введіть OTP", font=self.title_font).pack(pady=(20, 10))

        otp_entry = tk.Entry(self.root, font=self.label_font)
        otp_entry.pack(pady=pady, padx=padx)

        def submit_otp():
            otp = otp_entry.get()
            if self.auth_service.verify_otp(username, otp):
                messagebox.showinfo("Успішно", "Успішний вхід!")
                self.authorized_page()
            else:
                messagebox.showerror("Помилка", "Невірний OTP!")
                self.create_main_menu()

        tk.Button(self.root, text="Підтвердити OTP", font=self.button_font, command=submit_otp, width=15, height=2).pack(pady=(20, pady))
        tk.Button(self.root, text="Назад", font=self.button_font, command=self.create_main_menu, width=15, height=2).pack(pady=pady)

    def authorized_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        pady = 10
        padx = 10

        tk.Label(self.root, text="Вітаємо, Ви авторизовані!", font=self.title_font).pack(pady=(20, 10))

        # Кнопка "Вийти"
        tk.Button(self.root, text="Вийти", font=self.button_font, command=self.create_main_menu, width=20, height=2).pack(pady=(20, pady))
