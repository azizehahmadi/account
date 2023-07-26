from user.api.views import CreateUserView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('create/', CreateUserView, name='create'),
]

