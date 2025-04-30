from django.contrib.auth.models import User
from rest_framework import status
import pytest

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection

@pytest.mark.django_db
class TestCreateCollections:
    # @pytest.mark.skip #this test is skipped for now
    def test_if_user_is_anonymous_retrun_401(self, create_collection):
        response = create_collection({'title': 'a',})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_authenticate_retrun_403(self, api_client, create_collection):
        api_client.force_authenticate(user={})

        response = create_collection({'title': 'a',})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self,api_client,authenticate, create_collection):
        authenticate(is_staff=True)

        response = create_collection({'title': '',})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_retrun_201(self, authenticate, create_collection):
        authenticate(is_staff=True)

        response = create_collection({'title': 'a',})
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
        