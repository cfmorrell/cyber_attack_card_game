from django.urls import path
from . import views

app_name = "umpire"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("submit_red_cards/", views.submit_red_cards, name="submit_red_cards"),
    path("submit_blue_cards/", views.submit_blue_cards, name="submit_blue_cards"),
    path("get_adjudication/<int:turn_id>/", views.get_adjudication, name="get_adjudication"),
    path("submit_blue_cards/", views.submit_blue_cards, name="submit_blue_cards"),
    path("submit_red_cards/", views.submit_red_cards, name="submit_red_cards"),
    path("next_turn/", views.next_turn, name="next_turn"),
    path("reset_game/", views.reset_game, name="reset_game"),
]
