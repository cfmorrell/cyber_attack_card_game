from django.contrib import admin
from .models import *

class AttackCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'card_type')
    filter_horizontal = ('follows',)

class DefenseMatchupAdmin(admin.ModelAdmin):
    list_display = ('defense', 'attack')

admin.site.register(AttackCard, AttackCardAdmin)
admin.site.register(DefenseCard)
admin.site.register(Game)
admin.site.register(Turn)
admin.site.register(AttackChain)
admin.site.register(PlayedCard)
admin.site.register(Team)
admin.site.register(AttackDefenseMatchup, DefenseMatchupAdmin)
