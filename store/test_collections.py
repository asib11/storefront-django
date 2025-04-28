from rest_framework.test import APIClient
from rest_framework import status

class TestCreateCollections:
    def test_if_user_is_anonymous(self, client):
        client = APIClient()
        response = client.post('/store/collections/', {
            'title': 'a',
        })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED