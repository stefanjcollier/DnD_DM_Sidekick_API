from rest_framework import viewsets, mixins
from dnd_dm_sidekick_api.library.mixins import MultiSerializerMixin

from players.serializers import (ReputationSerializer, AdminReputationSerializer,
                                 CharacterCreationSerializer, CharacterViewSerializer,
                                 AdminCharacterSerializer)
from players.models import Reputation, Character


class ReputationView(viewsets.ModelViewSet):
  serializer_class = ReputationSerializer
  queryset = Reputation.objects.all()


class AdminReputationView(viewsets.ModelViewSet):
  serializer_class = AdminReputationSerializer
  queryset = Reputation.objects.all()


class CharacterView(MultiSerializerMixin, viewsets.ModelViewSet):
  serializer_classes = {
    'list': CharacterViewSerializer,
    'retrieve': CharacterViewSerializer,
  }
  default_serializer_class = CharacterCreationSerializer
  queryset = Character.objects.all()


class AdminCharacterView(viewsets.ReadOnlyModelViewSet):
  serializer_class = AdminCharacterSerializer
  queryset = Character.objects.all()

