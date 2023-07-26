# from rest_framework import generics
# from user.api.serializers import RegistrationSerializer
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.settings import api_settings
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# class CreateUserView(generics.CreateAPIView):
#     serializer_class = UserSerializer


# class CreateTokenView(ObtainAuthToken):
#     serializer_class = AuthTokenSerializer
#     renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

# @api_view(['POST', ])
# def CreateUserView(request):
#
#      if request.method == 'POST':
#          serializer = RegistrationSerializer(data=request.data)
#          if serializer.is_valid():
#              serializer.save()
#              return Response(serializer.data)
#


