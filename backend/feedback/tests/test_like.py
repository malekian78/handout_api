import pytest
from feedback.models import Like
from django.db.utils import IntegrityError

@pytest.mark.django_db
class TestLike:

    def test_like(self, handout, user):
        Like.objects.create(
            client_ip="127.22.22.110",
            user = user,
            handout = handout,
            )
        assert Like.objects.filter(user=user, handout=handout).exists()

    def test_duplicate_like(self, handout, user):
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
