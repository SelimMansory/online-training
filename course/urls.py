from course.apps import CourseConfig
from django.urls import path
from rest_framework.routers import DefaultRouter

from course.views import CourseViewSet, LessonDestroyAPIView, LessonUpdateAPIView, LessonCreateAPIView, \
    LessonListAPIView, LessonRetrieveAPIView, PaymentsListAPIView

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

app_name = CourseConfig.name

urlpatterns = [
                  # Lesson
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),

                  # Payments
                  path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),

              ] + router.urls