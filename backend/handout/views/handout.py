from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from handout.models import Handout
from handout.serializer import HandoutDetailSerializer, HandoutListSerializer


class HandoutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Handout.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["category", "author"]

    def get_serializer_class(self):
        if self.action == "list":
            return HandoutListSerializer
        return HandoutDetailSerializer
