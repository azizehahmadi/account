from django.shortcuts import render
from product.models import Product
from product.api.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from product.models import ProductBrand, ProductTag
from product.api.serializers import ProductBrandSerializer, ProductTagSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_detail(request, pk):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









class Brand_list(generics.ListCreateAPIView):
    queryset = ProductBrand.objects.all()
    serializer_class = ProductBrandSerializer


class Brand_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductBrand.objects.all()
    serializer_class = ProductBrandSerializer


class Tag_list(generics.ListCreateAPIView):
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer

class Tag_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductTag.objects.all()
    serializer_class = ProductSerializer