from flask import Flask, request, jsonify
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    user_name = data.get('user_name', 'Гость')
    return jsonify({'message': f'Привет, {user_name}! Спасибо за интерес к TG Мастер! Скоро с вами свяжутся.'})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))  # Используем PORT от Vercel или 5000 локально
    app.run(host='0.0.0.0', port=port, debug=True)