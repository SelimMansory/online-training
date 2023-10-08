from rest_framework import viewsets
from rest_framework.response import Response

from users.permission import IsUser, IsPermission
from users.seriliazers import UserSerializer, NoneUserSerializer
from users.models import User


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = NoneUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser, IsPermission]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance == request.user:
            serializer = UserSerializer(instance)
        else:
            serializer = NoneUserSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.filter(email=self.request.user), many=True)
        return Response(serializer.data)