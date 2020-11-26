from rest_framework import serializers
from players.models import Reputation
from shop.services import DiscountService


class ReputationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reputation
    fields = ('id', 'name', 'description')


class AdminReputationSerializer(serializers.ModelSerializer):
  price_modifier = serializers.SerializerMethodField('calc_reputation_bonus')

  def calc_reputation_bonus(self, reputation):
      return DiscountService.KEY_TO_BONUS[reputation.charisma_modifier]

  class Meta:
    model = Reputation
    fields = ('id', 'name', 'description', 'charisma_modifier', 'price_modifier')
