from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from course.models import Course, Lesson, Payments
from course.pagination import MyPagination
from course.permissions import IsStaffViewSet, IsStaff, IsUser
from course.seriliazers import CourseSerializer, LessonSerializer, PaymentsSerializer
from course.service import CreateMixin
from rest_framework.response import Response


# Create your views here.

class CourseViewSet(CreateMixin, viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsStaffViewSet]
    pagination_class = MyPagination

    def list(self, request, *args, **kwargs):
        if request.user.group == 'user':
            serializer = CourseSerializer(Course.objects.filter(owner=self.request.user), many=True)
            return Response(serializer.data)
        else:
            serializer = CourseSerializer(Course.objects.all(), many=True)
            return Response(serializer.data)


class LessonCreateAPIView(CreateMixin, generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsUser | IsAdminUser]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination

    def get_queryset(self):
        if self.request.user.group == 'user':
            queryset = Lesson.objects.filter(owner=self.request.user)
        elif self.request.user.group == 'staff':
            queryset = Lesson.objects.all()
        else:
            queryset = Lesson.objects.none()
        return queryset


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsUser | IsStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsUser | IsStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method')
    ordering_fields = ('date_of_payment',)
    permission_classes = [IsAuthenticated, IsStaff]
    pagination_class = MyPagination