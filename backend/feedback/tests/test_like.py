import pytest
from django.utils import timezone
from feedback.models import Like
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.contrib.auth import get_user_model
from handout.models import Handout, Author, Category, Tag
from django.db.utils import IntegrityError

@pytest.fixture
def author():
    return Author.objects.create(name="Author_Test")

@pytest.fixture
def user():
    return get_user_model().objects.create_user(
            email='testuserr@example.com', password='testpass'
        )

@pytest.fixture
def handout(author):
    category = Category.objects.create(name="Category Name")
    tag = Tag.objects.create(name="Tag Name")
    handout = Handout.objects.create(
        name="Handout",
        slug="theHandout",
        description="description of handout",
        page_count=10,
        publish_time = timezone.now(),
        author=author,
        file=SimpleUploadedFile("file.pdf", b"file_content", content_type="application/pdf"),
        )
    handout.category.add(category)
    handout.tag.add(tag)
    handout.save()
    return handout

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
