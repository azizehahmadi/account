from order.models import Order, OrderDetail
from rest_framework import viewsets
from order.api.serializers import OrderSerializer, OrderDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class OrderV(viewsets.ViewSet):

    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order_byId = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order_byId)
        return Response(serializer.data)

    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def update(self, request, pk):
        queryset = Order.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        queryset = Order.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class OrderDetailV(viewsets.ViewSet):

    def list(self, request):
        queryset = OrderDetail.objects.all()
        serializer = OrderDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = OrderDetail.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = OrderDetailSerializer(query)
        return Response(serializer.data)

    def create(self, request):
        serializer = OrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk):
        queryset = OrderDetail.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = OrderDetailSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        queryset = OrderDetail.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

