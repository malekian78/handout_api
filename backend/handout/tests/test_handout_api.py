import jdatetime
import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_get_category_fields_and_value_exist(client, handout, author, teardown_handouts):
    url = reverse("handout:handout-list")
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
        "description": "description of handout",
        "page_count": 10,
        "publish_time": str(jdatetime.date.today()),
        "author": author.name,
        # "file":""
    }

    # Only check the expected category item
    if item["id"] == handout.pk:
        for key, expected_value in expected_item.items():
            assert (
                item[key] == expected_value
            ), f"Value mismatch for '{key}' in item: {item}. Expected: {expected_value}, Actual: {item[key]}"


@pytest.mark.django_db
def test_handout_file_exists(client, handout, teardown_handouts):
    # Define the URL for the API endpoint that serves the handout data
    url = reverse("handout:handout-detail", kwargs={"pk": handout.pk})

    # Make a GET request to the API endpoint
    response = client.get(url)
    print("\n\n response:", response.json())

    # Ensure the request was successful
    assert response.status_code == status.HTTP_200_OK

    # Verify the file details in the response
    response_data = response.json()
    # assert 'file' in response_data  # Check if the file field exists in the response
    file_url = response_data["file"]
    assert file_url.endswith("file.pdf")  # Check if the file name matches

    # Additional assertions as per your requirements
    # For example, you can make another request to the file URL to ensure it is accessible
    print("file_url:", file_url)
    file_response = client.get(file_url)
    print("file response:", file_response)
    assert file_response.status_code == status.HTTP_200_OK
    assert file_response.content == b"file_content"  # Check the content of the file
