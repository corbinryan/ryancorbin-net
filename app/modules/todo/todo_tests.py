import unittest
import json

from app.modules.todo.controller import TodoController


def test_index():
    todo_controller = TodoController()
    result = todo_controller.index()
    assert result == {'message': 'Hello, World!'}
