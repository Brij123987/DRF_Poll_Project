from rest_framework import serializers
from polls.models import Polls, Choice, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fiels = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    votes  = VoteSerializer(many=True, required = False)

    class Meta:
        model = Choice
        fields = '__all__'

class PollsSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required = False)

    class Meta:
        model = Polls
        fields = '__all__'