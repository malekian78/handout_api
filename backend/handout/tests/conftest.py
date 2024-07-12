import pytest
from django.utils import timezone
from handout.models import Category, Handout, Author, Tag
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.fixture
def category():
    return Category.objects.create(
        name="cat1",
        slug="cat1",
        )

@pytest.fixture
def handout():
    author = Author.objects.create(name="Author Name")
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
