from rest_framework import serializers
from cartItem.models import CartItem, CartItemDetail
from product.models import Product

class cartItemDetailSerializer(serializers.ModelSerializer):

    total_cost = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CartItemDetail
        fields = ('id', 'quantity', 'product', 'cart_user', 'total_cost',)
    def get_total_cost(self, object):
        qun=object.quantity
        print(qun)
        ob = object.product.price
        price = qun*ob
        return price




class cartItemSerializer(serializers.ModelSerializer):

    cart_item = cartItemDetailSerializer(many=True, read_only=True, source='cart_user')

    class Meta:
        model = CartItem
        fields = ('id', 'customer', 'is_paid', 'payment_date', 'cart_item',)




