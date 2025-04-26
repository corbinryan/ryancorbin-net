from flask import render_template

class TodoController:
    def index(self):
        return render_template('todo/index.html', title="Todo App")

    def login(self):
        return render_template('todo/login.html', title="Todo App - Login")