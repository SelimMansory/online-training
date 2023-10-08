from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from subscribe.models import SubscribeUser
from subscribe.serializers import SubscribeSerializer


class SubscribeListAPIView(generics.ListAPIView):
    serializer_class = SubscribeSerializer
    queryset = SubscribeUser.objects.all()
    permission_classes = [IsAuthenticated]


class SubscribeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    queryset = SubscribeUser.objects.all()
    permission_classes = [IsAuthenticated]


class SubscribeDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscribeSerializer
    queryset = SubscribeUser.objects.all()
    permission_classes = [IsAuthenticated]