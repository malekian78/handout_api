import pytest
from django.urls import reverse

from feedback.models import Like


@pytest.mark.django_db
def test_user_can_like_handout(handout, user, teardown_handouts, auth_client):
    url = reverse("feedback:like-create-destroy", args=[handout.id])
    response = auth_client.post(url)
    assert Like.objects.filter(user=user, handout=handout).exists()
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_cannot_duplicate_like(handout, user, like, auth_client, teardown_handouts):
    url = reverse("feedback:like-create-destroy", args=[handout.id])
    response = auth_client.post(url)
    assert Like.objects.filter(user=user, handout=handout).count() == 1
    assert response.status_code == 400


@pytest.mark.django_db
def test_user_can_delete_like(auth_client, user, handout, like, teardown_handouts):
    url = reverse("feedback:like-create-destroy", args=[handout.id])
    response = auth_client.delete(url)
    assert response.status_code == 204
    assert not Like.objects.filter(user=user, handout=handout).exists()
