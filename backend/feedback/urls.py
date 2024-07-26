from django.urls import include, path
from rest_framework.routers import DefaultRouter

from feedback.views import CommentViewSet, LikeCreateDestroyView

app_name = "feedback"

router = DefaultRouter()
router.register(r"(?P<handout_id>\d+)/comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("like/<int:handout_id>/", LikeCreateDestroyView.as_view(), name="like-create-destroy"),
    path("", include(router.urls)),
]
