from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    tasks = [f"Вариант {i}" for i in range(1, 21)]
    return render_template('index.html', tasks=tasks)


@app.route('/task<int:task_id>.html')
def task(task_id):
    file_path = f"tasks/tasks{task_id}.txt"
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        questions = [line.strip() for line in lines if line.strip()]
    else:
        questions = ["нет задачи"]
    return render_template('task.html', task_id=task_id, questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
