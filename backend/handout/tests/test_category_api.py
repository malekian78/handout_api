from django.utils import timezone
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.mark.django_db
class TestCategoryApi:
    
    def test_get_category_response_200_status(self, api_client):
        url = reverse('handout:category-list')
        response = api_client.get(url)
        assert response.status_code == 200