from subscribe.apps import SubscribeConfig
from django.urls import path
from subscribe.views import SubscribeListAPIView, SubscribeCreateAPIView, SubscribeDestroyAPIView

app_name = SubscribeConfig.name

urlpatterns = [
    path('', SubscribeListAPIView.as_view(), name='subscribe_list'),
    path('create/', SubscribeCreateAPIView.as_view(), name='subscribe_create'),
    path('delete/<int:pk>', SubscribeDestroyAPIView.as_view(), name='subscribe_destroy'),
]