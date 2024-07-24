import os

import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone

from feedback.models import Like
from handout.models import Author, Category, Handout, Tag

User = get_user_model()


@pytest.fixture
def like():
    return Like.objects.create(
        client_ip="127.22.22.110",
        user=user,
        handout=handout,
    )


@pytest.fixture
def author():
    return Author.objects.create(name="Author_Test")


@pytest.fixture
def user():
    return User.objects.create_user(email="testuserr@example.com", password="testpass")


@pytest.fixture
def handout(author, category):
    tag = Tag.objects.create(name="Tag Name")
    handout = Handout.objects.create(
        name="Handout",
        slug="theHandout",
        description="description of handout",
        page_count=10,
        publish_time=timezone.now(),
        author=author,
        file=SimpleUploadedFile("file.pdf", b"file_content", content_type="application/pdf"),
    )

    handout.category.add(category)
    handout.tag.add(tag)
    handout.save()
    return handout


@pytest.fixture
def category():
    return Category.objects.create(
        name="cat1",
        slug="cat1",
    )


@pytest.fixture
def teardown_handouts():
    """Fixture to teardown any state that was created by test."""
    yield  # This will run the test
    # Teardown logic
    handouts = Handout.objects.all()
    for handout in handouts:
        if handout.file:
            file_path = handout.file.path
            if os.path.exists(file_path):
                os.remove(file_path)
        handout.delete()
