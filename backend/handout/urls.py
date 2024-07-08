from django.urls import path, include
from rest_framework.routers import DefaultRouter
from handout.views import CategoryViewSet

app_name = "handout"

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename="category")

urlpatterns = [
    path('', include(router.urls)),
]
