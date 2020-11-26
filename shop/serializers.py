from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ('id', 'name', 'weight', 'price_str', 'gp_price', 'sp_price')


class DiscountRequestSerializer(serializers.Serializer):
  reputation_id = serializers.IntegerField(min_value=0)
  charisma_modifier = serializers.IntegerField(min_value=-5, max_value=5)
