from rest_framework import viewsets

from players.serializers import ReputationSerializer, AdminReputationSerializer
from players.models import Reputation


class ReputationView(viewsets.ModelViewSet):
  serializer_class = ReputationSerializer
  queryset = Reputation.objects.all()


class AdminReputationView(viewsets.ModelViewSet):
  serializer_class = AdminReputationSerializer
  queryset = Reputation.objects.all()
