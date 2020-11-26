from django.db import models


class Reputation(models.Model):
  name = models.CharField(max_length=240, null=False, blank=False)
  description = models.TextField(null=True, blank=True)
  charisma_modifier = models.IntegerField(verbose_name='The equivalent charisma boost', null=False, blank=False)

