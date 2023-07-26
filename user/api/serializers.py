# from django.contrib.auth import get_user_model, authenticate
# from rest_framework import serializers
# from django.utils.translation import gettext as _
#
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model= get_user_model()
#         fields = ['email', 'password', 'name']
#         extra_kwargs = {
#             'password': {'write_only': True, 'min_length': 5}
#         }
#
#         def create(self, validate_data):
#             return get_user_model().objects.create(**validate_data)
#
#         def update(self, instance, validated_data):
#             password=validated_data.pop('password', None)
#             user= super().update(instance, validated_data)
#
#             if password:
#                 user.set_password(password)
#                 user.save()
#             return user






# class AuthTokenSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(style={
#         'input_type': 'password'
#     }, trim_whitespace=False)
#
#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')
#         user = authenticate(
#             request=self.context.get('request'),
#             username=email,
#             password=password
#         )
#         if not user:
#             msg =_('Unable to authenticate with provided credential')
#             raise serializers.ValidationError(msg, code=authorization)
#         attrs['user']=user
#         return attrs


# class RegistrationSerializer(serializers.ModelSerializer):
#
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#
#     def save(self):
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#
#         if password != password2:
#             raise serializers.ValidationError({'error': 'P1 and P2 should be same!'})
#
#         if User.objects.filter(email=self.validated_data['email']).exists():
#             raise serializers.ValidationError({'error': 'your email is already exist'})
#
#         account = User(email=self.validated_data['email'], username=self.validated_data['username'])
#         account.set_password(password)
#         account.save()
#         return account
