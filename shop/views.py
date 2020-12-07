from rest_framework import status
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from dnd_dm_sidekick_api.library.mixins import MultiSerializerMixin

from shop.serializers import ProductSerializer, ShopViewSerializer, ShopUpdateSerializer, DiscountRequestSerializer
from shop.models import Product, Shop
from shop.services import DiscountService


class ProductView(viewsets.ModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()


class ShopView(MultiSerializerMixin, viewsets.ModelViewSet):
  serializer_classes = {
    'list': ShopViewSerializer,
    'retrieve': ShopViewSerializer,
  }
  default_serializer_class = ShopUpdateSerializer
  queryset = Shop.objects.all()


class DiscountView(ViewSet):
  serializer_class = DiscountRequestSerializer

  def get_safe_data(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    return serializer.data

  def get_fields(self, request):
    data = self.get_safe_data(request)
    reputation_id     = data['reputation_id']
    charisma_modifier = data['charisma_modifier']
    return charisma_modifier, reputation_id

  # We're not creating but we want the URL tso be POST-ed to
  def create(self, request):
    charisma_modifier, reputation_id = self.get_fields(request)
    service = DiscountService(charisma_modifier, reputation_id)
    discount = service.discount()
    return Response({"discount": discount}, status=status.HTTP_200_OK)
