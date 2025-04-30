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