from django.urls import path
from handout.views import CategoryListCreateAPIView

urlpatterns = [
    # For APIView
    # path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    
    # For Generic Views
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    
]