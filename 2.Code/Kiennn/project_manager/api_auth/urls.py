from django.urls import path
from .views import LoginView, register, VerifyTokenView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', register, name='register'),
    path('verify_token', VerifyTokenView.as_view(), name='verify_token'),
]
