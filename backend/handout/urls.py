from django.urls import include, path
from rest_framework.routers import DefaultRouter

from handout.views import CategoryViewSet, HandoutViewSet

app_name = "handout"

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("list", HandoutViewSet, basename="handout")

urlpatterns = [
    path("", include(router.urls)),
]
