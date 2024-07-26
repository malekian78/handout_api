from rest_framework import serializers

from feedback.models import Comment
from handout.models import Handout


class handoutSrializer(serializers.ModelSerializer):
    class Meta:
        model = Handout
        fields = ["id", "name"]


class CommentSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    handout = handoutSrializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "handout", "name", "email", "body", "status"]
        read_only_fields = ["status"]

    def get_status(self, obj):
        return obj.get_status_display()
