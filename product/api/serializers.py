from rest_framework import serializers
from product.models import Product, ProductBrand, ProductTag
from rest_framework.validators import UniqueTogetherValidator
from cartItem.api.serializers import cartItemDetailSerializer
from order.api.serializers import OrderDetailSerializer

class ProductTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTag
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    cartItemDetail = cartItemDetailSerializer(many=True, read_only=True, source='cart_product')
    product_tag = ProductTagSerializer(many=True, read_only=True, source='product_tags')
    OrderDetail = OrderDetailSerializer(many=True, read_only=True, source='order_product')
    class Meta:
        model = Product
        fields = "__all__"


    def validate(self, data):
        if data['product_type'] == data['product_description']:
            raise serializers.ValidationError("the of product not be should the same of product description!")


class ProductBrandSerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=True, read_only=True, source='product_brand')

    class Meta:
        model = ProductBrand
        fields = "__all__"