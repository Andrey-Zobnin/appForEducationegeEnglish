from flask import Flask, render_template, request, redirect, url_for, flash
import json
import random


app = Flask(__name__)


# Загрузка пользователей из JSON файла
def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r', encoding='utf-8') as f:
            return json.load(f)

# Сохранение пользователей в JSON файл
def save_users(users):
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

# Загрузка задач из JSON файла
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
            print("Загруженные задачи из файла:", tasks)  # Отладочное сообщение
            return tasks
    return {}

tasks = load_tasks()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/task/<int:task_id>')
def task(task_id):
    task_data = tasks.get(str(task_id), {"questions": ["нет задачи"], "answers": []})
    return render_template('task.html', task_id=task_id, questions=task_data["questions"], answers=task_data["answers"])

@app.route('/random_task')
def random_task():
    task_id = random.choice(list(tasks.keys()))
    return task(task_id)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = load_users()
        
        # Проверка, существует ли пользователь с таким именем
        if username in users:
            flash('Пользователь с таким именем уже существует.')
            return redirect(url_for('register'))
        
        # Создание нового пользователя
        users[username] = {'password': password}
        save_users(users)
        
        flash('Регистрация прошла успешно. Теперь вы можете войти.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = load_users()
        
        if username in users and users[username]['password'] == password:
            flash('Вы успешно вошли в систему.')
            return redirect(url_for('index'))
        else:
            flash('Неверное имя пользователя или пароль.')
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)