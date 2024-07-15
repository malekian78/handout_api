import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_category_fields_exist(client, category):
    url = reverse("handout:category-list")
    response = client.get(url)
    actual_data = response.json()
    expected_fields = {"id", "name", "slug", "parent", "children"}

    for item in actual_data:
        # Check that the fields match exactly
        assert (
            set(item.keys()) == expected_fields
        ), f"Fields mismatch in item: {item}. Expected fields: {expected_fields}"

        # Check the values if necessary
        expected_item = {
            "id": category.pk,
            "name": "cat1",
            "slug": "cat1",
            "parent": None,
            "children": [],  # Adjust according to your actual data structure
        }

        # Only check the expected category item
        if item["id"] == category.pk:
            for key, expected_value in expected_item.items():
                assert (
                    item[key] == expected_value
                ), f"Value mismatch for '{key}' in item: {item}. Expected: {expected_value}, Actual: {item[key]}"


@pytest.mark.django_db
def test_get_category_detail_fields_exist(client, category):
    url = reverse("handout:category-detail", kwargs={"pk": 1})
    response = client.get(url)
    actual_data = response.json()
    expected_data = {"id": category.pk, "name": "cat1", "slug": "cat1", "parent": None, "children": []}

    assert set(actual_data.keys()) == set(
        expected_data.keys()
    ), f"Fields mismatch. Expected: {set(expected_data.keys())}, Actual: {set(actual_data.keys())}"

    for key, expected_value in expected_data.items():
        assert (
            actual_data[key] == expected_value
        ), f"Value mismatch for '{key}'. Expected: {expected_value}, Actual: {actual_data[key]}"
