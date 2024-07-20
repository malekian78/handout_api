from rest_framework import serializers

from feedback.models import Like


class LikeSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(many=False, read_only=True, slug_field="email")
    # handout = serializers.SlugRelatedField(many=False, read_only=True, slug_field="name")
    class Meta:
        model = Like
        fields = ["id", "client_ip", "user", "handout"]
