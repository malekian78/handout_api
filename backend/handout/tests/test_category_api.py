import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from handout.models import Category

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def category():
    return Category.objects.create(
        name="cat1",
        slug="cat1",
        )

@pytest.mark.django_db
class TestCategoryApi:
    
    def test_get_category_response_200_status(self, api_client):
        url = reverse('handout:category-list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_get_category_detail_response_200_status(self, api_client, category):
        url = reverse('handout:category-detail', kwargs={'pk':1})
        response = api_client.get(url)
        assert response.status_code == 200