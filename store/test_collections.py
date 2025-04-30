from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
import pytest

@pytest.mark.django_db
class TestCreateCollections:
    # @pytest.mark.skip #this test is skipped for now
    def test_if_user_is_anonymous_retrun_401(self):
        client = APIClient()
        response = client.post('/store/collections/', {
            'title': 'a',
        })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_authenticate_retrun_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {
            'title': 'a',
        })
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/store/collections/', {
            'title': '',
        })
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_retrun_201(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/store/collections/', {
            'title': 'a',
        })
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
        