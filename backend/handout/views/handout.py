from rest_framework import viewsets

from handout.models import Handout
from handout.serializer import HandoutSerializer


class HandoutViewSet(viewsets.ModelViewSet):
    queryset = Handout.objects.all()
    serializer_class = HandoutSerializer
