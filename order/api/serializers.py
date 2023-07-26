from rest_framework import serializers
from order.models import Order, OrderDetail



class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    orderDetail = OrderDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = "__all__"

