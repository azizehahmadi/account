from rest_framework import serializers
from category.models import Category
from product.api.serializers import ProductSerializer

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    product = ProductSerializer(many=True, read_only=True, source='product_categories')
    class Meta:
        model = Category
        fields = ['url', 'pk', 'title', 'is_active', 'is_delete', 'product']






