from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from handout.models import Category
from handout.serializer import CategorySerializer, DetailCategorySerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = DetailCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "slug"
    
    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        object.delete()
        return Response({"detail": "successfully removed"})