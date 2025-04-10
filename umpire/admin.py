from django.contrib import admin
from .models import Card, GameSession, Turn, PlayedCard

admin.site.register(Card)
admin.site.register(GameSession)
admin.site.register(Turn)
admin.site.register(PlayedCard)
