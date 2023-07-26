from django.urls import path
from .views import RegisterUserView, EmailActiveCodeView, HomePageView, LoginView, \
    ProfileUserView, ChangePasswordView, SendRestPasswordEmailView, PasswordRestView



urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify-email/<str:uid>/<str:token>/', EmailActiveCodeView.as_view(), name='email-verification'),
    path('home/', HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', ProfileUserView.as_view(), name='me'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('send-email-rest-password/', SendRestPasswordEmailView.as_view(), name='send-email-rest-password'),
    path('rest-password/<str:uid>/<str:token>/', PasswordRestView.as_view(), name='rest-password'),



]