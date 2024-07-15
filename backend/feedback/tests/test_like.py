import pytest
from django.db.utils import IntegrityError

from feedback.models import Like


@pytest.mark.django_db
def test_user_can_like_handout(handout, user, teardown_handouts):
    Like.objects.create(
        client_ip="127.22.22.110",
        user=user,
        handout=handout,
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
