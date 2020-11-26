from rest_framework import viewsets

from players.serializers import ReputationSerializer
from players.models import Reputation


class ReputationView(viewsets.ModelViewSet):
  serializer_class = ReputationSerializer
  queryset = Reputation.objects.all()
