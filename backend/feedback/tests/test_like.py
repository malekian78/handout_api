import pytest
from feedback.models import Like
from django.db.utils import IntegrityError

@pytest.mark.django_db
def test_like(handout, user):
    Like.objects.create(
        client_ip="127.22.22.110",
        user = user,
        handout = handout,
        )
    assert Like.objects.filter(user=user, handout=handout).exists()

@pytest.mark.django_db
def test_duplicate_like(handout, user):
    Like.objects.create(
        client_ip="127.22.22.110",
        user=user,
        handout=handout,
    )
    with pytest.raises(IntegrityError):
            Like.objects.create(
                client_ip="127.22.22.110",
                user=user,
                handout=handout,
            )
