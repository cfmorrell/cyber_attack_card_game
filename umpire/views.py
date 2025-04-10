from django.shortcuts import render
from django.http import HttpResponse
from collections import namedtuple, defaultdict
from umpire.models import GameSession, Turn, Card, PlayedCard
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from umpire.utils import get_playable_red_cards, build_attack_chains, adjudicate_red_card

def dashboard(request):
    # Get active game session
    game = GameSession.objects.filter(is_active=True).order_by("-created").first()
    if not game:
        game = GameSession.objects.create(name="Default Session")

    # Get or create the first turn for this game
    turn = Turn.objects.filter(game=game).order_by("-number").first()
    if not turn:
        turn = Turn.objects.create(game=game, number=1, blue_budget=70)
    print(f"📦 Dashboard Turn ID: {turn.id}, Number: {turn.number}")
    played_ids = PlayedCard.objects.filter(turn__game=game).values_list("card_id", flat=True)
    red_played = PlayedCard.objects.filter(turn__game=game, team="red").order_by("turn__number", "id")
    attack_chains = build_attack_chains(red_played)

    context = {
    "turn": turn,
    "next_turn_number": turn.number + 1,
    "game": game,
    "red_cards": get_playable_red_cards(game, turn),
    "red_played": red_played,
    "attack_chains": attack_chains,
    "blue_cards": Card.objects.filter(team="blue").exclude(id__in=played_ids),
    "blue_played": PlayedCard.objects.filter(turn__game=game, team="blue"),
    "blue_budget": turn.blue_budget or 70,  # Fallback
    "sp_active": PlayedCard.objects.filter(turn__game=game, team="blue", card__name="Security Platform").exists(),
    "chains": [],  # Optional for now
    }

    return render(request, "umpire/dashboard.html", context)

@csrf_exempt  # Optional: for testing HTMX
def submit_blue_cards(request):
    if request.method == "POST":
        game = GameSession.objects.filter(is_active=True).order_by("-created").first()
        turn = game.turns.order_by("-number").first()

        # Remove previous plays for Blue Team this turn
        PlayedCard.objects.filter(turn=turn, team="blue").delete()

        # Save new plays
        card_ids = request.POST.getlist("blue_cards")
        for cid in card_ids:
            card = Card.objects.get(id=cid)
            PlayedCard.objects.create(turn=turn, card=card, team="blue")

    # Re-render just the Blue Team form + active cards
    played_ids = PlayedCard.objects.filter(turn__game=game).values_list("card_id", flat=True)
    blue_played = PlayedCard.objects.filter(turn__game=game, team="blue")
    sp_active = blue_played.filter(card__name="Security Platform").exists()
    blue_cards = Card.objects.filter(team="blue").exclude(id__in=played_ids)

    context = {
        "blue_cards": blue_cards,
        "blue_played": blue_played,
        "blue_budget": turn.blue_budget,
        "sp_active": sp_active,
    }

    return render(request, "umpire/partials/blue_card_form.html", context)

@csrf_exempt
def submit_red_cards(request):
    if request.method == "POST":
        game = GameSession.objects.filter(is_active=True).order_by("-created").first()
        turn = game.turns.order_by("-number").first()

        # Remove existing plays
        PlayedCard.objects.filter(turn=turn, team="red").delete()

        # Save new plays
        card_ids = request.POST.getlist("red_cards")
        for cid in card_ids:
            card = Card.objects.get(id=cid)
            PlayedCard.objects.create(turn=turn, card=card, team="red")

    played_ids = PlayedCard.objects.filter(turn__game=game).values_list("card_id", flat=True)
    red_played = PlayedCard.objects.filter(turn__game=game, team="red").order_by("turn__number", "id")
    attack_chains = build_attack_chains(red_played)
    print(f"✅ Saved red card '{card.name}' for turn ID: {turn.id}, number: {turn.number}")

    context = {
        # "red_cards": red_cards,
        # "red_played": red_played,
        "red_cards": get_playable_red_cards(game, turn),
        "red_played": red_played,
        "attack_chains": attack_chains,
    }

    return render(request, "umpire/partials/red_card_form.html", context)

@require_POST
def next_turn(request):
    game = GameSession.objects.filter(is_active=True).order_by("-created").first()
    current_turn = game.turns.order_by("-number").first()

    # Calculate carryover
    played = PlayedCard.objects.filter(turn=current_turn, team="blue")
    spent = sum([card.card.cost for card in played])
    carryover = current_turn.blue_budget - spent

    next_number = current_turn.number + 1
    new_turn = Turn.objects.create(game=game, number=next_number, blue_budget=70 + carryover)

    return redirect("umpire:dashboard")

@require_POST
def reset_game(request):
    # Get the current active game
    game = GameSession.objects.filter(is_active=True).order_by("-created").first()

    if game:
        # Delete all turns and played cards
        game.turns.all().delete()

        # Recreate Turn 1 with default budget
        Turn.objects.create(game=game, number=1, blue_budget=70)

    return redirect("umpire:dashboard")

def get_adjudication(request, turn_id):
    turn = Turn.objects.get(id=turn_id)
    game = turn.game

    # All blue cards played so far (defenses persist)
    blue_cards_all = PlayedCard.objects.filter(turn__game=game, team="blue").select_related("card")
    active_blue_card_names = [p.card.name for p in blue_cards_all]

    # Red cards across all turns, grouped by turn number
    red_cards_all = PlayedCard.objects.filter(turn__game=game, team="red").select_related("card", "turn").order_by("turn__number", "id")

    adjudicated_by_turn = defaultdict(list)

    for red_card in red_cards_all:
        result = adjudicate_red_card(red_card.card.name, active_blue_card_names)
        adjudicated_by_turn[red_card.turn.number].append(result)

    print("🧪 Adjudicating by turn:")
    for turn_num, items in adjudicated_by_turn.items():
        print(f"  Turn {turn_num}: {[r['card'] for r in items]}")
        
    context = {
        "turn": turn,
        "adjudicated_by_turn": dict(adjudicated_by_turn)
    }

    return render(request, "umpire/partials/adjudication_panel.html", context)
