from rest_framework import serializers

from handout.models import Handout, Tag
from handout.serializer import CategoryDetailSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]


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
