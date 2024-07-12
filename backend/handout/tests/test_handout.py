import pytest
import os
from handout.models import Handout

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
