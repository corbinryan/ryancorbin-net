import json

class TestTodo():
    def test_index(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert response.json == {'message': 'Hello, World!'}
            