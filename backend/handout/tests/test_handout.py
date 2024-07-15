import pytest


@pytest.mark.django_db
def test_handout_file_name(handout, teardown_handouts):
    assert handout.file_name == "file"


@pytest.mark.django_db
def test_user_can_change_file_name(handout, teardown_handouts):
    handout.file_name = "test_file"
    handout.save()
    assert handout.file_name == "test_file"


@pytest.mark.django_db
def test_handout_file_size(handout, teardown_handouts):
    assert handout.file_size == handout.file.size
