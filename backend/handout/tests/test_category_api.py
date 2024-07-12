import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_get_category_fields_exist(client, category):
    url = reverse('handout:category-list')
    response = client.get(url)
    actual_data = response.json()
    expected_fields = {'id', 'name', 'slug', 'parent', 'children'}
    for item in actual_data:
        assert expected_fields.issubset(item.keys()), f"Missing fields in item: {item}"

@pytest.mark.django_db
def test_get_category_detail_fields_exist(client, category):
    url = reverse('handout:category-detail', kwargs={'pk':1})
    response = client.get(url)
    actual_data = response.json()
    expected_fields = {'id', 'name', 'slug', 'parent', 'children'}
    assert expected_fields.issubset(actual_data.keys()), f"Missing fields in item: {actual_data}"

