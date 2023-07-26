from rest_framework.views import APIView
from category.models import Category
from category.api.serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status


class CategoryListAV(APIView):

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAV(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except category.DoesNotExist:
            return Response({'error': 'data is not Found'}, status=status.HTTP_200_OK)

        serializer = CategorySerializer(category,  context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_200_OK)








