import pytest
from django.urls import reverse

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
