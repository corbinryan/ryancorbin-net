import unittest
import json

from src.ryancorbin_net.modules.todo.controller import TodoController


def test_index():
    todo_controller = TodoController()
    result = todo_controller.index()
    assert result == {'message': 'Hello, World!'}
