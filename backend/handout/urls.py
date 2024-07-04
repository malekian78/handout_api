from django.urls import path
from handout.views import CategoryListCreateAPIView, CategoryDetailApiView

app_name = "handout"

urlpatterns = [
    # Generic Views for Detail of Category
    path('categories/<slug:slug>/', CategoryDetailApiView.as_view(), name='category-detail'),
    # Generic Views for list of Category
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list')
]