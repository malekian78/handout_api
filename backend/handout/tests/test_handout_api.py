import jdatetime
import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_get_handout_list_fields_and_value_exist(client, handout, author, teardown_handouts):
    url = reverse("handout:handout-list")
    response = client.get(url)
    actual_data = response.json()
    expected_fields = {
        "id",
        "name",
        "slug",
        "visit_count",
        "publish_time",
        "author",
        "category",
        "tag",
    }

    for item in actual_data:
        # Check that the fields match exactly
        assert (
            set(item.keys()) == expected_fields
        ), f"Fields mismatch in item: {item}. Expected fields: {expected_fields}"

    # Check the values if necessary
    expected_item = {
        "id": handout.pk,
        "name": "Handout",
        "slug": "theHandout",
        "visit_count": handout.visit_count,
        "publish_time": str(jdatetime.date.today()),
        "author": {"id": author.id, "name": author.name},
        "category": [
            {"id": category.id, "name": category.name, "slug": category.slug} for category in handout.category.all()
        ],
        "tag": [{"id": tag.id, "name": tag.name, "slug": tag.slug} for tag in handout.tag.all()],
    }
    print("author:", handout.author)

    # Only check the expected handout item
    if item["id"] == handout.pk:
        for key, expected_value in expected_item.items():
            assert (
                item[key] == expected_value
            ), f"Value mismatch for '{key}' in item: {item}. Expected: {expected_value}, Actual: {item[key]}"


@pytest.mark.django_db
def test_get_handout_detail_fields_and_value_exist(client, handout, author, teardown_handouts):
    url = reverse("handout:handout-detail", kwargs={"pk": handout.pk})
    response = client.get(url)
    actual_data = response.json()
    expected_fields = {
        "id",
        "name",
        "description",
        "slug",
        "page_count",
        "visit_count",
        "publish_time",
        "author",
        "file_size",
        "file_name",
        "file",
        "category",
        "tag",
        "like_count",
    }

    # Check that all expected fields are present in the response
    assert (
        set(actual_data.keys()) == expected_fields
    ), f"Expected fields: {expected_fields}, but got: {set(actual_data.keys())}"

    # Construct the absolute URL for the file
    file_url = f"http://testserver{handout.file.url}"

    # Check the values if necessary
    expected_data = {
        "id": handout.pk,
        "name": "Handout",
        "slug": "theHandout",
        "description": "description of handout",
        "page_count": 10,
        "publish_time": str(jdatetime.date.today()),
        "author": {"id": author.id, "name": author.name},
        "category": [
            {"id": category.id, "name": category.name, "slug": category.slug} for category in handout.category.all()
        ],
        "tag": [{"id": tag.id, "name": tag.name, "slug": tag.slug} for tag in handout.tag.all()],
        "file_size": handout.file_size,
        "file_name": handout.file_name,
        "file": file_url,
        "like_count": 0,
    }

    # Check that the values of the expected fields match
    for field, value in expected_data.items():
        assert (
            actual_data[field] == value
        ), f"For field '{field}', expected value '{value}' but got '{actual_data[field]}'"


@pytest.mark.django_db
def test_handout_file_exists(client, handout, teardown_handouts):
    url = reverse("handout:handout-detail", kwargs={"pk": handout.pk})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    # Check if the file field exists in the response
    file_url = response_data["file"]
    assert file_url.endswith("file.pdf")
