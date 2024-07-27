import pytest
from django.urls import reverse
from rest_framework import status

from feedback.models import Comment


@pytest.mark.django_db
def test_create_comment(client, handout, teardown_handouts):
    url = reverse("feedback:comments-list", kwargs={"handout_id": handout.id})
    data = {"name": "Test Comment", "email": "testuserr@example.com", "body": "This is a test comment"}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data
    assert response.data["name"] == data["name"]
    assert response.data["email"] == data["email"]
    assert response.data["body"] == data["body"]


@pytest.mark.django_db
def test_list_comments(client, handout, comment, teardown_handouts):
    url = reverse("feedback:comments-list", kwargs={"handout_id": handout.id})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["id"] == comment.id
    assert response.data[0]["name"] == comment.name
    assert response.data[0]["email"] == comment.email
    assert response.data[0]["body"] == comment.body


@pytest.mark.django_db
def test_retrieve_comment(client, handout, comment, teardown_handouts):
    url = reverse("feedback:comments-detail", kwargs={"handout_id": handout.id, "pk": comment.id})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == comment.id
    assert response.data["name"] == comment.name
    assert response.data["email"] == comment.email
    assert response.data["body"] == comment.body


@pytest.mark.django_db
def test_delete_comment(client, handout, comment, teardown_handouts):
    url = reverse("feedback:comments-detail", kwargs={"handout_id": handout.id, "pk": comment.id})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Comment.objects.filter(id=comment.id).exists()
