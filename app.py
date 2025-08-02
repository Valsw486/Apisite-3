from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Запрашиваем случайную цитату с API
    try:
        response = requests.get('https://zenquotes.io/api/random')
        if response.status_code == 200:
            data = response.json()
            # API возвращает список из одного элемента
            quote_data = data[0]
            quote = quote_data.get('q', 'Цитата не найдена')
            author = quote_data.get('a', 'Неизвестен')
        else:
            quote = 'Не удалось получить цитату.'
            author = ''
    except Exception as e:
        quote = 'Ошибка при запросе цитаты.'
        author = ''

    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)