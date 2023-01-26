from django.urls import path
from .views import LoginWithPassword, TestAPI, RegisterAPI, MainRequestAPI
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login', LoginWithPassword.as_view()),
    path('test', TestAPI.as_view()),
    path('register', RegisterAPI.as_view()),
    path('main-request', MainRequestAPI.as_view()),
    path('logout', TokenBlacklistView.as_view(), name='token_blacklist'),
]