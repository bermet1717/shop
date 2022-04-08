from rest_framework import serializers

from applications.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'images', 'owner', 'description', 'price', 'category')