from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from feedback.models import Like
from feedback.serializer import LikeSerializer


class LikeCreateDestroyView(mixins.CreateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "handout_id"

    def post(self, request, *args, **kwargs):
        handout_id = self.kwargs["handout_id"]
        data = {
            "handout": handout_id,
        }
        serializer = self.get_serializer(data=data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        client_ip = self.get_client_ip(request)
        Like_handout = get_object_or_404(Like, handout=self.kwargs["handout_id"], user=user, client_ip=client_ip)
        Like_handout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_client_ip(request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip
