from rest_framework import serializers
from players.models import Reputation, Character
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


class CharacterCreationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Character
    fields = ('id', 'name', 'charisma_modifier', 'reputation', 'remote_image_url')


class CharacterViewSerializer(CharacterCreationSerializer):
  reputation = ReputationSerializer()


class AdminCharacterSerializer(serializers.ModelSerializer):
  reputation = ReputationSerializer()
  discount = serializers.SerializerMethodField('calc_discount')

  def calc_discount(self, instance):
    return DiscountService.from_character(instance).discount()

  class Meta:
    model = Character
    fields = ('id', 'name', 'charisma_modifier', 'reputation', 'remote_image_url', 'discount')
