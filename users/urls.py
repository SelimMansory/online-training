from rest_framework.routers import DefaultRouter
from django.urls import path
from users.apps import UsersConfig
from users.views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

app_name = UsersConfig.name

urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

              ] + router.urls