from rest_framework.views import APIView
from cartItem.models import CartItem, CartItemDetail
from cartItem.api.serializers import cartItemSerializer, cartItemDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from customer.api.serializers import CustomerSerializer
from customer.models import Customer
from product.models import Product
from django.shortcuts import get_object_or_404


class cartItemListAV(APIView):

    def get(self, request):
        cartItem = CartItem.objects.all()
        serializer = cartItemSerializer(cartItem, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = cartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class cartItemById(APIView):

    def get(self, request, pk):

        cartItem = get_object_or_404(CartItem, pk=pk)
        serializer = cartItemSerializer(cartItem)
        return Response(serializer.data)


    def put(self, request, pk):
        cartItem = CartItem.objects.get(pk=pk)
        serializer = cartItemSerializer(cartItem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        cartItem = CartItem.objects.get(pk=pk)
        cartItem.delete()
        return Response(status=status.HTTP_200_OK)





class cartItemDetailListAV(APIView):

    def get(self, request):
        cart_detail = CartItemDetail.objects.all()
        serializer = cartItemDetailSerializer(cart_detail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = cartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class cartItemDetailById(APIView):
    def get(self, request, pk):
        try:
            cart_detail = CartItemDetail.objects.get(pk=pk)
        except cart_detail.DoesNotExist:
            return Response({'error': 'cartDetail Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = cartItemDetailSerializer(cart_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        cart_detail = CartItemDetail.objects.get(pk=pk)
        serializer = cartItemDetailSerializer(cart_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cart_detail = CartItemDetail.objects.get(pk=pk)
        cart_detail.delete()
        return Response(status=status.HTTP_200_OK)


class customer_cartDetail(generics.ListAPIView):
    serializer_class = cartItemDetailSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return CartItemDetail.objects.filter(cart_user=pk)


class customer_cartDetail_create(generics.CreateAPIView):
    serializer_class = cartItemDetailSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        cartItem = CartItem.objects.get(pk=pk)
        serializer.save(cart_user=cartItem)



class cat_cart_Item(generics.ListAPIView):

    serializer_class = cartItemDetailSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return CartItemDetail.objects.filter(product=pk)


class cat_cart_Item_create(generics.CreateAPIView):
    serializer_class = cartItemDetailSerializer

    def perform_create(self, serializer):
        pk= self.kwargs.get('pk')
        cat_Item = Product.objects.get(pk=pk)
        serializer.save(product=cat_Item)











