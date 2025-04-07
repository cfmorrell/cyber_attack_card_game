from rest_framework import serializers
from .models import AttackCard, DefenseCard, Game, Turn, AttackChain, PlayedCard, Team

class AttackCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttackCard
        fields = '__all__'

class DefenseCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefenseCard
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = '__all__'

class AttackChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttackChain
        fields = '__all__'

class PlayedCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayedCard
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
