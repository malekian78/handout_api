import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_get_category_response_200_status(api_client):
    url = reverse('handout:category-list')
    response = api_client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_category_detail_response_200_status(api_client, category):
    url = reverse('handout:category-detail', kwargs={'pk':1})
    response = api_client.get(url)
    assert response.status_code == 200
