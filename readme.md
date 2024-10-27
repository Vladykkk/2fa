# Двофакторна Автентифікація (2FA) з Використанням Tkinter

Ця програма реалізує просту систему двофакторної автентифікації (2FA) з використанням графічного інтерфейсу на базі **Tkinter**. Вона дозволяє користувачам зареєструватися, увійти в систему за допомогою імені користувача та пароля, а також ввести OTP (одноразовий пароль), який генерується під час входу.

## Особливості

- **Реєстрація користувачів**: Користувачі можуть зареєструвати новий обліковий запис з ім'ям користувача та паролем.
- **Вхід в систему**: Після успішної автентифікації користувач отримує OTP, який він має ввести для завершення процесу входу.
- **Генерація OTP**: OTP генерується для кожного користувача під час спроби входу.
- **Графічний інтерфейс**: Програма використовує бібліотеку Tkinter для забезпечення зручного графічного інтерфейсу.

## Вимоги

- Python 3.x
- Бібліотеки:
  - Tkinter (вбудовано в стандартну бібліотеку Python)
  - `pyotp` для генерації OTP

## Встановлення

1. Клонуйте репозиторій або завантажте архів з проєктом:

   \`\`\`bash
   git clone https://github.com/your-repo/2fa-tkinter.git
   \`\`\`

2. Перейдіть до папки з проєктом:

   \`\`\`bash
   cd 2fa
   \`\`\`

3. Встановіть необхідні залежності:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Використання

1. Запустіть програму, виконавши наступну команду:

   \`\`\`bash
   python main.py
   \`\`\`

2. Після запуску програми відкриється вікно з можливістю:

   - Зареєструвати нового користувача.
   - Увійти за допомогою імені користувача та пароля.
   - Ввести OTP, щоб завершити процес входу.

3. **Реєстрація**:

   - Введіть ім'я користувача та пароль для реєстрації нового облікового запису.

4. **Вхід**:

   - Введіть ім'я користувача та пароль для перевірки автентичності.
   - Після цього згенерується OTP, який потрібно ввести для входу.

5. **OTP**:
   - Введіть одноразовий пароль (OTP), який ви отримаєте під час входу.