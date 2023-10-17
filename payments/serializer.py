from rest_framework import serializers

from payments.models import PaymentsCourse, CheckPayment


class PaymentsCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsCourse
        fields = ('course', 'payment_url', 'id')


class CheckPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckPayment
        fields = ('checkout_id', 'payment_status',)