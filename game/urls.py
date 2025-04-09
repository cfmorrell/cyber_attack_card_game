from django.urls import path, include
from rest_framework import routers
from . import views
from .views import PlayTurnView


router = routers.DefaultRouter()
router.register(r'attack_cards', views.AttackCardViewSet)
router.register(r'defense_cards', views.DefenseCardViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'turns', views.TurnViewSet)
router.register(r'attack_chains', views.AttackChainViewSet)
router.register(r'played_cards', views.PlayedCardViewSet)
router.register(r'teams', views.TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('play_turn/', PlayTurnView.as_view(), name='play_turn'),
]
