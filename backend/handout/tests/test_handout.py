import pytest
from django.utils import timezone
from handout.models import Category, Handout, Author, Tag
from django.core.files.uploadedfile import SimpleUploadedFile
import os

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

@pytest.mark.django_db
class TestHandout:
    def teardown_method(self, method):
        """ Teardown any state that was created by test """
        handouts = Handout.objects.all()
        for handout in handouts:
            if handout.file:
                file_path = handout.file.path
                if os.path.exists(file_path):
                    os.remove(file_path)
            handout.delete()

    def test_handout_file_name(self, handout):
        assert handout.file_name == "file"

    def test_handout_file_name_change(self, handout):
        handout.file_name = "test_file"
        assert handout.file_name == "test_file"

    def test_handout_file_size(self, handout):
        assert handout.file_size == handout.file.size

