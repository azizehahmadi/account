from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .Utils import Utile
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, \
    ChangePasswordSerializer, SendEmailForRestPasswordSerializer, PasswordResetSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from . import models
from django.contrib.auth.hashers import check_password
import requests

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class RegisterUserView(APIView):

    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            verification_link = request.build_absolute_uri(f'http://127.0.0.1:8000/user/verify-email/{uid}/{token}/')

            # send email
            body = 'your verification link:' + verification_link
            data = {
                'subject': 'verification link',
                'body': body,
                'to_email': user.email
            }
            Utile.send_email(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


User = get_user_model()
class EmailActiveCodeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uid, token):
        try:
            id = force_str((urlsafe_base64_decode(uid)))
            user = User.objects.get(id=id)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'error', 'Invalid Token'}, status=status.HTTP_404_NOT_FOUND)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            # tokens = get_tokens_for_user(user)
            # access_token = tokens['access']
            # refresh_token = tokens['refresh']
            # redirect_url = reverse('home')
            # response = HttpResponseRedirect(redirect_url)
            # response.headers['Authorization'] = f'Bearer {access_token}'
            # response.set_cookie(key='refresh_token', value=refresh_token)
            # return response
            return HttpResponseRedirect(reverse('home'))

        else:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_200_OK)

class HomePageView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    def get(self, request):
        return Response({'msg': 'validation successful'})

class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            phone = serializer.data.get('phone')
            password = serializer.data.get('password')
            user = authenticate(
                email=email,
                phone=phone,
                password=password
            )
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'login successful'}, status=status.HTTP_200_OK)
            return Response({'error': 'login failed'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileUserView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            return Response({'msg': 'the change is save'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendRestPasswordEmailView(APIView):

    def post(self, request):
        serializer = SendEmailForRestPasswordSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'msg': 'Password Reset send please check your email!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordRestView(APIView):

    def post(self, request, uid, token):
        serializer = PasswordResetSerializer(data=request.data, context={'uid': uid, 'token': token})
        if serializer.is_valid():
            return Response({'msg': 'your password reset'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)