import pytest
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from handout.models import Handout, Author, Category, Tag
from django.contrib.auth import get_user_model

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
