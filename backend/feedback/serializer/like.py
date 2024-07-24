from rest_framework import serializers

from feedback.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "client_ip", "user", "handout"]
        read_only_fields = ["client_ip", "user"]

    def create(self, validated_data):
        request = self.context.get("request", None)
        user = request.user if request and request.user.is_authenticated else None
        client_ip = request.META.get("REMOTE_ADDR") if request else None
        handout = validated_data.get("handout")

        like_instance, created = Like.objects.get_or_create(
            user=user,
            handout=handout,
            defaults={
                "client_ip": client_ip,
            },
        )

        if not created:
            # If the Like instance already exists, raise an error or handle as needed
            raise serializers.ValidationError({"detail": "You have already liked this handout."})

        return like_instance
