from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from course.models import Course
from payments.models import PaymentsCourse, CheckPayment
from payments.serializer import PaymentsCourseSerializer, CheckPaymentSerializer
from payments.service import create_payment, payment_verification


# Create your views here.


class PaymentsCourseCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsCourseSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        pk = request.data['course']
        course = Course.objects.filter(pk=pk).first()
        checkout = create_payment(course.title, course.price)
        request.data['payment_url'] = checkout[0]
        request.data['checkout_id'] = checkout[1]
        data = super().post(request, *args, **kwargs)
        CheckPayment.objects.create(
            checkout_id=checkout[1],
            payment_status='unpaid'
        )
        return data


class PaymentsCourseListAPIView(generics.ListAPIView):
    serializer_class = PaymentsCourseSerializer
    queryset = PaymentsCourse.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class CheckPaymentRetrieveAPIVieww(generics.RetrieveAPIView):
    serializer_class = CheckPaymentSerializer
    queryset = CheckPayment.objects.all()
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        data = super().retrieve(request, *args, **kwargs)
        payment_status = payment_verification(data.data['checkout_id'])
        data.data['payment_status'] = payment_status
        return data