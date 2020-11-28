from django.db import models


class ReputationManager(models.Manager):
  def get_default(self):
    return self.get(charisma_modifier=0)


class Reputation(models.Model):
  objects = ReputationManager()

  name = models.CharField(max_length=240, null=False, blank=False)
  description = models.TextField(null=True, blank=True)
  charisma_modifier = models.IntegerField(verbose_name='The equivalent charisma boost', null=False, blank=False)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['charisma_modifier']


class Character(models.Model):
  name = models.CharField(max_length=240, null=False, blank=False)
  charisma_modifier = models.IntegerField(null=False, blank=False)
  reputation = models.ForeignKey(Reputation, default=Reputation.objects.get_default().id, on_delete=models.SET_DEFAULT)

  def __str__(self):
    return self.name
