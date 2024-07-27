from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from feedback.models import Comment
from feedback.serializer import CommentSerializer
from handout.models import Handout


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        handout_id = self.kwargs.get("handout_id")
        handout = get_object_or_404(Handout, id=handout_id)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(handout=handout, status=Comment.Status.DRAFT)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "comment not created."}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        handout_id = self.kwargs.get("handout_id")
        filtered_queryset = self.queryset.filter(handout_id=handout_id, status=Comment.Status.PUBLISHED)
        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        handout_id = self.kwargs.get("handout_id")
        comment_id = self.kwargs.get("pk")
        comment = get_object_or_404(Comment, handout_id=handout_id, id=comment_id, status=Comment.Status.PUBLISHED)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            request.data["email"] = user.email
        return super().update(request, *args, **kwargs)
