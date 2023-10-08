from rest_framework import serializers

from subscribe.models import SubscribeUser


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscribeUser
        fields = ('subscribe', 'course', 'user',)