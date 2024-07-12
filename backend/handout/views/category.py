from rest_framework import viewsets
from handout.models import Category
from handout.serializer import CategorySerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample

@extend_schema(
    operation_id='listCategories',
    tags=['Category'],
    summary='Retrieve a list of categories',
    description='Returns a list of all categories in the system.',
    responses={
        200: OpenApiResponse(response=CategorySerializer(many=True), description='A list of categories'),
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
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    @extend_schema(
        operation_id='retrieveCategory',
        tags=['Category'],
        summary='Retrieve a category',
        description='Returns the details of a specific category.',
        responses={
            200: CategorySerializer,
            404: OpenApiResponse(description='Category not found'),
        },
        examples=[
            OpenApiExample(
                'Retrieve Category Example',
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

