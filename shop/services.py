from django.shortcuts import get_object_or_404

from players.models import Reputation


class DiscountService:
  def __init__(self, character_charisma, reputation_id):
    self.character_charisma = character_charisma
    self.reputation_id = reputation_id

  @staticmethod
  def from_character(character):
    return DiscountService(character.charisma_modifier, character.reputation_id)

  KEY_TO_BONUS = {
    -5: 1.1,
    -4: 1.08,
    -3: 1.05,
    -2: 1.03,
    -1: 1.02,
     0: 1,
     1: 0.98,
     2: 0.95,
     3: 0.93,
     4: 0.90,
     5: 0.85,
  }

  def discount(self):
    """
    :throws: Reputation.DoesNotExist
    :return: Double - between 0 and 2
    """
    charisma_bonus = self.KEY_TO_BONUS[self.character_charisma]
    if charisma_bonus < -5:
      charisma_bonus = -5
    if charisma_bonus > 5:
      charisma_bonus = 5
    reputation = Reputation.objects.get(pk=self.reputation_id)
    reputation_bonus = self.KEY_TO_BONUS[reputation.charisma_modifier]
    return charisma_bonus * reputation_bonus

