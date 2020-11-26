from django.contrib import admin

from players.models import Reputation


class ReputationAdmin(admin.ModelAdmin):
  list_display = ('name', 'charisma_modifier')


admin.site.register(Reputation, ReputationAdmin)
