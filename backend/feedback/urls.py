from django.urls import include, path
from rest_framework.routers import DefaultRouter

from feedback.views import LikeViewSet

app_name = "feedback"

router = DefaultRouter()
router.register(r"handouts/(?P<handout_id>\d+)/likes", LikeViewSet, basename="handout-likes")

urlpatterns = [
    path("", include(router.urls)),
]
