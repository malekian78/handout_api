from django.urls import path

from feedback.views import LikeCreateDestroyView

app_name = "feedback"

# router = DefaultRouter()
# router.register(r"(?P<handout_id>\d+)/likes", LikeViewSet, basename="handout-likes")

urlpatterns = [
    path("like/<int:handout_id>/", LikeCreateDestroyView.as_view(), name="like-create-destroy"),
]
