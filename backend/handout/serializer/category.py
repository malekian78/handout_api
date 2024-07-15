from rest_framework import serializers

from handout.models import Category


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class CategorySerializer(serializers.ModelSerializer):
    parent = CategoryDetailSerializer(read_only=True)
    children = CategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "parent", "children"]
