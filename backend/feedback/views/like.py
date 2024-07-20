from django.db import models
from django.db.models import Func
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from feedback.models import Like
from feedback.serializer import LikeSerializer
from handout.models import Handout


class CastToInet(Func):
    function = "CAST"
    template = "%(function)s(%(expressions)s AS inet)"


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        handout_id = self.kwargs["handout_id"]
        return Like.objects.filter(handout_id=handout_id)

    # def create(self, request, *args, **kwargs):
    #     print("\n_________________________________________\n")
    #     handout = get_object_or_404(Handout, id=self.kwargs['handout_id'])
    #     print("handout:",handout)
    #     user = request.user if request.user.is_authenticated else None
    #     print("user:",user.email)
    #     client_ip = request.META.get('REMOTE_ADDR')
    #     print("client_ip:",client_ip)

    #     serializer = LikeSerializer(data=request.data)
    #     print("serializer.is_valid()::",serializer.is_valid())
    #     if serializer.is_valid():
    #         print(serializer.data)
    #         print("client_ip from frontend:", serializer.data['client_ip'])
    #     # isExist = Like.objects.filter(handout=handout, user=user, client_ip=client_ip)
    #     # isExist = Like.objects.filter(handout=handout, user=user, client_ip=serializer.data['client_ip'])
    #     # Cast client_ip to text
    #     client_ip_filter = Like.objects.annotate(client_ip_as_text=CastAsText('client_ip', CharField())).filter(
    #         handout=handout, user=user, client_ip_as_text=client_ip)
    #     print("isExist:",client_ip_filter)
    #     print("isExist:",client_ip_filter.exists())
    #     return Response({"detail": "Like added."}, status=status.HTTP_201_CREATED)
    #     # Check if the like already exists
    #     # if Like.objects.filter(handout=handout, user=user, client_ip=client_ip).exists():
    #     #     return Response({"detail": "Like already exists."}, status=status.HTTP_400_BAD_REQUEST)

    #     like = Like(handout=handout, user=user, client_ip=client_ip)
    #     like.save()
    #     return Response({"detail": "Like added."}, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        client_ip = request.META.get("REMOTE_ADDR")
        # user = request.user if request.user.is_authenticated else None
        # handout_id = self.kwargs["handout_id"]
        ip_address = "203.0.113.42"

        allLikes = Like.objects.all()

        print("allLikes[0]:", allLikes[0].client_ip)
        print("allLikes[0]:", type(allLikes[0].client_ip))

        client_ip = request.META.get("REMOTE_ADDR")
        print("client_ip:", client_ip)
        print("type client_ip:", type(client_ip))

        like_Exist = Like.objects.filter(client_ip=client_ip)

        ip_address = "172.0.113.42"

        print("CastToInet(Value(ip_address))::", models.expressions.RawSQL("CAST(%s AS inet)", (ip_address,)))
        # testing = CastToInet(Value(ip_address))
        # likes_with_ip = Like.objects.extra(where=["client_ip = CAST(%s AS inet)"], params=[ip_address])
        # Use Q objects for complex lookups
        # like_query = Like.objects.filter(
        #     Q(client_ip=client_ip)
        # )

        print("___________________________\n")
        print("like_query:", like_Exist)
        return Response({"detail": "Already liked"}, status=status.HTTP_200_OK)

        # like, created = Like.objects.get_or_create(
        #     client_ip=client_ip,
        #     user=user,
        #     handout_id=handout_id,
        # )

        # if created:
        #     return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response({"detail": "Already liked"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["delete"])
    def unlike(self, request, handout_id=None):
        handout = get_object_or_404(Handout, id=handout_id)
        user = request.user if request.user.is_authenticated else None
        client_ip = request.META.get("REMOTE_ADDR")

        # Check if the like exists
        like = Like.objects.filter(handout=handout, user=user, client_ip=client_ip).first()
        if like is None:
            return Response({"detail": "Like does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"detail": "Like removed."}, status=status.HTTP_204_NO_CONTENT)
