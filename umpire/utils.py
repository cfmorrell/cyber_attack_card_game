from django.db.models import Count
from collections import defaultdict
from .models import Card, PlayedCard
from .rules import ATTACK_CHAIN_RULES

def get_playable_red_cards(game, turn):
    # All red plays in the game so far
    red_plays_all = PlayedCard.objects.filter(turn__game=game, team="red").select_related("card")
    red_plays_this_turn = red_plays_all.filter(turn=turn)

    all_red_cards = Card.objects.filter(team="red")

    # Build chains from all prior plays
    attack_chains = build_attack_chains(red_plays_all)
    chain_heads = [chain[-1] for chain in attack_chains if chain]

    # Determine which chains have already been extended this turn
    chains_extended_this_turn = set()
    for chain in attack_chains:
        if not chain:
            continue
        last_card = chain[-1]
        if red_plays_this_turn.filter(card__name=last_card).exists():
            chains_extended_this_turn.add(last_card)

    # Determine valid next cards based on current chain heads
    valid_next_card_names = set()
    for head in chain_heads:
        if head not in chains_extended_this_turn:
            valid_next_card_names.update(ATTACK_CHAIN_RULES.get(head, []))

    # Add all available yellow cards (to allow new chains)
    played_counts = red_plays_all.values("card_id").annotate(total=Count("id"))
    played_map = {entry["card_id"]: entry["total"] for entry in played_counts}

    yellow_cards = Card.objects.filter(team="red", card_type="yellow")
    available_yellow_card_names = []
    for card in yellow_cards:
        if played_map.get(card.id, 0) < card.quantity:
            available_yellow_card_names.append(card.name)

    valid_next_card_names.update(available_yellow_card_names)

    # Final filter: only include cards that are valid next steps AND not exhausted
    available_card_ids = []
    for card in all_red_cards:
        if card.name in valid_next_card_names:
            if played_map.get(card.id, 0) < card.quantity:
                available_card_ids.append(card.id)

    return Card.objects.filter(id__in=available_card_ids)


def build_attack_chains(played_cards):
    chains = []
    current_chains = []

    for play in played_cards.order_by("turn__number", "id"):
        card = play.card
        card_name = card.name

        if card.card_type == "yellow":
            current_chains.append([card_name])
        elif card.card_type in ["red", "black"]:
            added = False
            for chain in current_chains:
                last_card = chain[-1]
                if card_name in ATTACK_CHAIN_RULES.get(last_card, []):
                    chain.append(card_name)
                    added = True
                    break
            if not added:
                current_chains.append([card_name])

    chains.extend(current_chains)
    return chains

def adjudicate_red_card(card_name, active_blue_cards):
    from .rules import DEFENSE_EFFECTIVENESS

    effectiveness = DEFENSE_EFFECTIVENESS.get(card_name, {})
    blocked = []
    detected = []

    for blue_card in active_blue_cards:
        if blue_card in effectiveness.get("blocked_by", []):
            blocked.append(blue_card)
        if blue_card in effectiveness.get("detected_by", []):
            detected.append(blue_card)

    status = []
    if blocked:
        status.append("blocked")
    if detected:
        status.append("detected")

    return {
        "card": card_name,
        "status": status,
        "defenders": {
            "blocked": blocked,
            "detected": detected
        },
        "symptom": effectiveness.get("symptom")
    }
