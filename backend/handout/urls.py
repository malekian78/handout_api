from django.urls import include, path
from rest_framework.routers import DefaultRouter

from handout.views import CategoryViewSet

app_name = "handout"

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
