from flask import Blueprint, redirect, request, session, url_for
from .controller import TodoController


todo_bp = Blueprint('todo', __name__)
todo_controller = TodoController()

@todo_bp.route('/', methods=['GET'])
def index():
  if 'username' in session:
    return todo_controller.index()
  else:
    return redirect(url_for('todo.login'))

@todo_bp.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    session['username'] = request.form['username']
    return redirect(url_for('todo.index'))
  return todo_controller.login()

@todo_bp.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('todo.index'))