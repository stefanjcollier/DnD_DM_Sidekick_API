from rest_framework import serializers
from players.models import Reputation


class ReputationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reputation
    fields = ('id', 'name', 'description')
