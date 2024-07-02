from rest_framework import generics
from handout.models import Category
from handout.serializer import CategorySerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer