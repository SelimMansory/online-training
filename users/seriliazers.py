from rest_framework import serializers

from subscribe.serializers import SubscribeSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id', 'email', 'city', 'phone', 'first_name', 'last_name', 'password', 'avatar', 'group',)


class NoneUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'city', 'phone',)