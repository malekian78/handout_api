from rest_framework import serializers

from handout.models import Handout


class HandoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handout
        fields = [
            "id",
            "name",
            "description",
            "page_count",
            "visit_count",
            "publish_time",
            "author",  # TODO: foreign key
            "file_size",
            "file_name",
            "file",
            "category",  # TODO:
            "tag",  # TODO
        ]
