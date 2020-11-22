from rest_framework import viewsets

from shop.serializers import ProductSerializer
from shop.models import Product


class ItemView(viewsets.ModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
