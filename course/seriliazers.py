from rest_framework import serializers
from course.models import Course, Lesson, Payments
from course.validators import URLValidator
from subscribe.serializers import SubscribeSerializer
from users.seriliazers import UserSerializer
from subscribe.models import SubscribeUser


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [URLValidator(field='video_url')]


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscribe = SubscribeSerializer(source='subscribeuser_set', many=True, read_only=True)

    def get_count_lesson(self, instance):
        return Lesson.objects.filter(course__id=instance.id).count()

    class Meta:
        model = Course
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Payments
        fields = ('user', 'date_of_payment', 'payment_amount', 'payment_method',)