from django.contrib import admin

# Register your models here.

from FightGame.models import *

class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end', 'category']

class CombatAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'tournament', 'date', 'winner']

class BichoAdmin(admin.ModelAdmin):
    list_display = ['alias', 'skills', 'force', 'resistance']
    list_filter = ['skills']
    search_fields = ['alias']

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Combat, CombatAdmin)
admin.site.register(Bicho, BichoAdmin)
