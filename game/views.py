from rest_framework import viewsets
from .models import AttackCard, DefenseCard, Game, Turn, AttackChain, PlayedCard, Team
from .serializers import (
    AttackCardSerializer, DefenseCardSerializer, GameSerializer,
    TurnSerializer, AttackChainSerializer, PlayedCardSerializer, TeamSerializer
)

class AttackCardViewSet(viewsets.ModelViewSet):
    queryset = AttackCard.objects.all()
    serializer_class = AttackCardSerializer

class DefenseCardViewSet(viewsets.ModelViewSet):
    queryset = DefenseCard.objects.all()
    serializer_class = DefenseCardSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class TurnViewSet(viewsets.ModelViewSet):
    queryset = Turn.objects.all()
    serializer_class = TurnSerializer

class AttackChainViewSet(viewsets.ModelViewSet):
    queryset = AttackChain.objects.all()
    serializer_class = AttackChainSerializer

class PlayedCardViewSet(viewsets.ModelViewSet):
    queryset = PlayedCard.objects.all()
    serializer_class = PlayedCardSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
