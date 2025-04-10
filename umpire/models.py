from django.db import models

class Card(models.Model):
    TEAM_CHOICES = [
        ('red', 'Red Team'),
        ('blue', 'Blue Team'),
    ]

    TYPE_CHOICES = [
        ('yellow', 'Initial'),
        ('red', 'Intermediate'),
        ('black', 'Final'),
        ('defense', 'Defense'),
    ]

    name = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=5, choices=TEAM_CHOICES)
    card_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    cost = models.IntegerField(default=0)  # only used by Blue Team cards
    sp_required = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=1)  # Number of times this card can appear in a game

    def __str__(self):
        return self.name

class GameSession(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Turn(models.Model):
    game = models.ForeignKey(GameSession, on_delete=models.CASCADE, related_name='turns')
    number = models.IntegerField()
    blue_budget = models.IntegerField(default=70)

    def __str__(self):
        return f"Turn {self.number} – {self.game.name}"


class PlayedCard(models.Model):
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE, related_name='plays')
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    team = models.CharField(max_length=5, choices=Card.TEAM_CHOICES)
    chain_id = models.IntegerField(null=True, blank=True)  # to associate cards in the same chain
    is_flipped = models.BooleanField(default=False)  # for blocked attack cards

    def __str__(self):
        return f"{self.card.name} ({self.team}) – Turn {self.turn.number}"
