from rest_framework import serializers
from customer.models import Customer
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from cartItem.api.serializers import cartItemSerializer
from order.api.serializers import OrderSerializer

class CustomerSerializer(serializers.ModelSerializer):
    cart_customer = cartItemSerializer(many=True, read_only=True)
    order = OrderSerializer(many=True, read_only=True, )
    class Meta:

        model = Customer

        fields =('id',
                 'customer_name',
                 'customer_last_name',
                 'customer_address',
                 'customer_post_code',
                 'customer_phone', 'cart_customer', 'order',)


    customer_post_code = serializers.IntegerField(validators=[
        UniqueValidator(queryset=Customer.objects.all())
    ])

    def validate(self, data):
        if data['customer_post_code'] == data['customer_phone']:
            raise serializers.ValidationError("post code and phone number cant be the same!")


    