from rest_framework import serializers
from . import models
from rest_framework.validators import UniqueValidator
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes, force_str
from .Utils import Utile
import re


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = models.User
        fields = ('email', 'phone', 'username', 'password', 'password2',)
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8, 'max_length': 12}
        }

    def validate_email(self, value):
        if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", value):
            print(f"The email address {value} is not valid")
            raise serializers.ValidationError('the email address not valid!')
        if models.User.objects.filter(email__iexact=value).exists():
            return serializers.ValidationError('this email is already exist!')
        return value

    def validate_phone(self, number: str):

        number_pattern = re.compile(r'^(?:\+98|0)\d{10}$')
        if number_pattern.match(number):
                if number.startswith('0'):
                    return '+98' + number[1:]
                return number
        else:
            raise serializers.ValidationError({'phone': 'Incorrect phone number.'})

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError('P1 and P2 is not match!')

        return attrs

    def create(self, validated_data):
        if models.User.objects.filter(phone__iexact=validated_data['phone']).exists():
            raise serializers.ValidationError('this phone number is already taken')

        return models.User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = models.User
        fields = ('email', 'phone', 'password')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('email', 'phone', 'username')


class ChangePasswordSerializer(serializers.Serializer):

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        fields = ('password', 'password2')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')

        if password != password2:
            raise serializers.ValidationError('P1 and P2 not matched!')
        user.set_password(password)
        user.save()
        return attrs


class SendEmailForRestPasswordSerializer(serializers.Serializer):

   email = serializers.EmailField(max_length=255)

   class Meta:
       fields = ('email',)

   def validate(self, attrs):
       email = attrs.get('email')

       if models.User.objects.filter(email__iexact=email).exists():
           user = models.User.objects.get(email=email)
           uid = urlsafe_base64_encode(force_bytes(user.id))
           token = PasswordResetTokenGenerator().make_token(user)

           link = 'http://127.0.0.1:8000/user/rest-password/'+uid + '/' + token

           # send email
           body = 'link: ' + link
           data = {
               'subject': 'Rest your password',
               'body': body,
               'to_email': user.email

           }
           Utile.send_email(data)
           return attrs
       else:
           serializers.ValidationError('email not found!')


class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        fields = ('password', 'password2')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        uid = self.context.get('uid')
        token = self.context.get('token')

        if password != password2:
            raise serializers.ValidationError('P1 and P2 does not match!')
        id = urlsafe_base64_decode(force_str(uid))
        user = models.User.objects.get(id=id)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError('token is Expired!')
        user.set_password(password)
        user.save()
        return attrs

