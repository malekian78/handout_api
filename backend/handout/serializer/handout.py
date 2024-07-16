from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from handout.models import Handout, Tag
from handout.serializer import CategoryDetailSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Handout List Example",
            value={
                "id": 1,
                "name": "mamad1",
                "slug": "mamad",
                "visit_count": 0,
                "publish_time": "1403-03-30",
                "author": "ali",
                "category": [{"id": 1, "name": "دیجیتالی", "slug": "digital"}],
                "tag": [{"id": 1, "name": "tag1", "slug": "tag1"}, {"id": 2, "name": "tag2", "slug": "tag2"}],
            },
        ),
        OpenApiExample(
            "Handout Detail Example",
            value={
                "id": 1,
                "name": "mamad1",
                "description": "test description",
                "slug": "mamad",
                "page_count": 5,
                "visit_count": 0,
                "publish_time": "1403-03-30",
                "author": "ali",
                "file_size": 113120,
                "file_name": "agahi2",
                "file": "http://127.0.0.1:8000/media/handouts/ali/agahi2.pdf",
                "category": [{"id": 1, "name": "دیجیتالی", "slug": "digital"}],
                "tag": [{"id": 1, "name": "tag1", "slug": "tag1"}, {"id": 2, "name": "tag2", "slug": "tag2"}],
            },
        ),
    ]
)
class HandoutSerializer(serializers.ModelSerializer):
    category = CategoryDetailSerializer(many=True)
    tag = TagSerializer(many=True)
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field="name")

    class Meta:
        model = Handout
        fields = [
            "id",
            "name",
            "description",
            "slug",
            "page_count",
            "visit_count",
            "publish_time",
            "author",
            "file_size",
            "file_name",
            "file",
            "category",
            "tag",
        ]

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        # if handout-list
        if not request.parser_context.get("kwargs").get("pk"):
            rep.pop("description", None)
            rep.pop("page_count", None)
            rep.pop("file_size", None)
            rep.pop("file_name", None)
            rep.pop("file", None)

        return rep
