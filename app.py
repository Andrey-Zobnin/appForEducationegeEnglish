from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import json

app = Flask(__name__)
app.secret_key = 'andy_2020'  # Необходимо для работы с сессиями

login_manager = LoginManager()
login_manager.init_app(app)

# file path
USER_DATA_FILE = 'users.json'

# Загрузка данных пользователей из файла
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

# Сохранение данных пользователей в файл
def save_users(users):
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f)

@login_manager.user_loader
def load_user(username):
    users = load_users()
    return users.get(username)

@app.route('/')
def home():
    tasks = [f"Вариант {i}" for i in range(1, 21)]
    return render_template('index.html', tasks=tasks)

@app.route('/task<int:task_id>.html')
@login_required
def task(task_id):
    file_path = f"tasks/tasks{task_id}.txt"
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        questions = [line.strip() for line in lines if line.strip()]
    else:
        questions = ["нет задачи"]
    return render_template('task.html', task_id=task_id, questions=questions)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='sha256')
        users = load_users()
        if username in users:
            flash('Пользователь с таким именем уже существует.')
            return redirect(url_for('register'))
        users[username] = {'password': password, 'correct_answers': 0}
        save_users(users)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            login_user(user)
            return redirect(url_for('home'))
        flash('Неверное имя пользователя или пароль')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/update_score', methods=['POST'])
@login_required
def update_score():
    data = request.get_json()
    users = load_users()
    if data['correct']:
        users[current_user.username]['correct_answers'] += 1
        save_users(users)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)