import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_get_category_response_200_status(client, category):
    url = reverse('handout:category-list')
    response = client.get(url)
    print("url:",url)
    actual_data = response.json()
    expected_fields = {'id', 'name', 'slug', 'parent', 'children'}
    print("actual_data:",actual_data)
    for item in actual_data:
        assert expected_fields.issubset(item.keys()), f"Missing fields in item: {item}"

@pytest.mark.django_db
def test_get_category_detail_response_200_status(client, category):
    url = reverse('handout:category-detail', kwargs={'pk':1})
    response = client.get(url)
    assert response.status_code == 200
