from rest_framework import viewsets
from .models import AttackCard, DefenseCard, Game, Turn, AttackChain, PlayedCard, Team
from .serializers import (
    AttackCardSerializer, DefenseCardSerializer, GameSerializer,
    TurnSerializer, AttackChainSerializer, PlayedCardSerializer, TeamSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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



class PlayTurnView(APIView):
    def post(self, request):
        data = request.data
        game = Game.objects.get(id=data["game_id"])
        turn = Turn.objects.get(id=data["turn_id"])
        team = Team.objects.get(id=data["team_id"])
        card_ids = data["card_ids"]

        if team.role == "RED":
            if len(card_ids) != 3:
                return Response({"error": "Red Team must play exactly 3 attack cards."}, status=status.HTTP_400_BAD_REQUEST)

            # Validate and create a new chain
            chain = AttackChain.objects.create(game=game, active=True)

            cards = [AttackCard.objects.get(id=cid) for cid in card_ids]
            for card in cards:
                PlayedCard.objects.create(turn=turn, team=team, card_attack=card, chain=chain)

        elif team.role == "BLUE":
            total_cost = 0
            defense_cards = []

            for cid in card_ids:
                card = DefenseCard.objects.get(id=cid)
                total_cost += card.cost
                defense_cards.append(card)

            if total_cost > team.budget:
                return Response({"error": f"Not enough budget. Needed: {total_cost}, Available: {team.budget}"},
                                status=status.HTTP_400_BAD_REQUEST)

            # Deduct and roll over remaining budget
            team.budget -= total_cost
            team.save()

            for card in defense_cards:
                PlayedCard.objects.create(turn=turn, team=team, card_defense=card)

        return Response({"message": "Turn submitted successfully"}, status=status.HTTP_201_CREATED)

from django.shortcuts import render, get_object_or_404
from .models import Game, Turn, Team, AttackCard, DefenseCard

def umpire_panel(request):
    games = Game.objects.all()
    selected_game = None
    red_team = None
    blue_team = None
    turn = None
    attack_cards = []
    defense_cards = []
    budget = 0

    if request.method == "POST":
        # Process form submission (handled later)
        pass

    if "game_id" in request.GET:
        selected_game = get_object_or_404(Game, id=request.GET["game_id"])
        red_team = selected_game.teams.filter(role="RED").first()
        blue_team = selected_game.teams.filter(role="BLUE").first()
        turn = selected_game.turns.order_by("-number").first()
        attack_cards = AttackCard.objects.all()
        defense_cards = DefenseCard.objects.all()
        budget = blue_team.budget if blue_team else 0

    return render(request, "game/umpire_panel.html", {
        "games": games,
        "selected_game": selected_game,
        "red_team": red_team,
        "blue_team": blue_team,
        "turn": turn,
        "attack_cards": attack_cards,
        "defense_cards": defense_cards,
        "budget": budget,
    })
