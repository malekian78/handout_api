from rest_framework import viewsets

from handout.models import Category
from handout.serializer import CategorySerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialize
    @extend_schema(
        operation_id='DetailCategory',
        tags=['Category'],
        summary='Detail of a category',
        description='Returns the details of a specific category base on id.',
        responses={
            200: CategorySerializer,
            404: OpenApiResponse(description='Category not found'),
        },
        examples=[
            OpenApiExample(
                'Category Detail Example',
                value={'id': 1, 'name': 'Electronics', 'slug': 'electronics', 'parent': None, 'children': []}
            )
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        operation_id='listCategories',
        tags=['Category'],
        summary='Retrieve a list of categories',
        description='Returns a list of all categories in the system.',
        responses={
            200: CategorySerializer(many=True),
        },
        examples=[
            OpenApiExample(
                'Category List Example',
                value=[
                    {'id': 1, 'name': 'Electronics', 'slug': 'electronics', 'parent': None, 'children': []},
                    {'id': 2, 'name': 'Books', 'slug': 'books', 'parent': None, 'children': []}
                ]
            )
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

