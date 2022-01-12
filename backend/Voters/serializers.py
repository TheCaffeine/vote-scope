from backend.Voters.models import County, Voters
from rest_framework import serializers
from Voters.models import County, Voters

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('CountyId',
                  'CountyName')

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voters
        fields = ('VoterId',
                  'VoterName',
                  'County',
                  'DateOfJoining',
                  'PhotoFileName')