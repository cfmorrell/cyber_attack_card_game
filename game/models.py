from django.db import models

class Team(models.Model):
    TEAM_CHOICES = [
        ('RED', 'Red Team'),
        ('BLUE', 'Blue Team'),
    ]
    name = models.CharField(max_length=10, choices=TEAM_CHOICES)

    def __str__(self):
        return self.name

class AttackCard(models.Model):
    CARD_TYPE_CHOICES = [
        ('YELLOW', 'Initial Attack'),
        ('RED', 'Intermediate Attack'),
        ('BLACK', 'Final Attack'),
    ]

    name = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    card_type = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES)
    follows = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='next_cards')

    def __str__(self):
        return f"{self.name} ({self.card_type})"

class DefenseCard(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    cost = models.PositiveIntegerField()
    requires_sp = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.cost} points"

class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Game {self.id} - {'Active' if self.active else 'Complete'}"

class Turn(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='turns')
    turn_number = models.PositiveIntegerField()
    budget_remaining = models.PositiveIntegerField(default=70)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Game {self.game.id} - Turn {self.turn_number}"

class AttackChain(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='attack_chains')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Chain {self.id} - {'Active' if self.active else 'Blocked'}"

class PlayedCard(models.Model):
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE, related_name='played_cards')
    card_attack = models.ForeignKey(AttackCard, null=True, blank=True, on_delete=models.SET_NULL)
    card_defense = models.ForeignKey(DefenseCard, null=True, blank=True, on_delete=models.SET_NULL)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    chain = models.ForeignKey(AttackChain, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        card = self.card_attack or self.card_defense
        return f"{card.name} played by {self.team.name}"

class AttackDefenseMatchup(models.Model):
    attack = models.ForeignKey('AttackCard', on_delete=models.CASCADE)
    defense = models.ForeignKey('DefenseCard', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.defense.name} counters {self.attack.name}"
