from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from handout.models import Category


@extend_schema_serializer(
    examples=[OpenApiExample("Category Detail Example", value={"id": 1, "name": "Electronics", "slug": "electronics"})]
)
class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Category Example",
            value={"id": 1, "name": "Electronics", "slug": "electronics", "parent": None, "children": []},
        ),
        OpenApiExample(
            "Category with Children Example",
            value={
                "id": 2,
                "name": "Computers",
                "slug": "computers",
                "parent": {"id": 1, "name": "Electronics", "slug": "electronics"},
                "children": [],
            },
        ),
    ]
)
class CategorySerializer(serializers.ModelSerializer):
    parent = CategoryDetailSerializer(read_only=True)
    children = CategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "parent", "children"]
