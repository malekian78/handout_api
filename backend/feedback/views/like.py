from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from feedback.models import Like
from feedback.serializer import LikeSerializer
from handout.models import Handout


class LikeCreateDestroyView(
    mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView
):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "handout_id"

    def post(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        handout_id = self.kwargs["handout_id"]
        client_ip = request.META.get("REMOTE_ADDR")
        like_Exist_user = Like.objects.filter(handout_id=handout_id, user=user)
        like_Exist_clientIp = Like.objects.filter(handout_id=handout_id, client_ip=client_ip)

        if like_Exist_clientIp or like_Exist_user:
            return Response({"detail": "Already liked"}, status=status.HTTP_200_OK)
        else:
            created = Like.objects.create(
                client_ip=client_ip,
                user=user,
                handout_id=handout_id,
            )
            if created:
                return Response({"detail": "new like added."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"detail": "Some Error ocured"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        print("HHHHHHHHHIIIIIII")
        handout = get_object_or_404(Handout, id=self.kwargs["handout_id"])
        user = request.user if request.user.is_authenticated else None
        client_ip = request.META.get("REMOTE_ADDR")

        like = Like.objects.filter(handout=handout, user=user, client_ip=client_ip).first()
        if like is None:
            return Response({"detail": "Like does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
