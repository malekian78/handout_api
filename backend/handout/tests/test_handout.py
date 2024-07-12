import pytest
import os
from handout.models import Handout

@pytest.mark.django_db
def teardown_method(method):
    """ Teardown any state that was created by test """
    handouts = Handout.objects.all()
    for handout in handouts:
        if handout.file:
            file_path = handout.file.path
            if os.path.exists(file_path):
                os.remove(file_path)
        handout.delete()

@pytest.mark.django_db
def test_handout_file_name(handout):
    assert handout.file_name == "file"

@pytest.mark.django_db
def test_handout_file_name_change(handout):
    handout.file_name = "test_file"
    assert handout.file_name == "test_file"

@pytest.mark.django_db
def test_handout_file_size(handout):
    assert handout.file_size == handout.file.size
