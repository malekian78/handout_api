from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from handout.models import Handout
from handout.serializer import HandoutSerializer


class HandoutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Handout.objects.all()
    serializer_class = HandoutSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["category", "author"]
