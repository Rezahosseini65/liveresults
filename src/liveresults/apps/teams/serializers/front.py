from rest_framework import serializers

from liveresults.apps.teams.models import Team, Honor


class TeamFrontRetrieveSerializer(serializers.ModelSerializer):
    league = serializers.CharField(source='league.name')

    class Meta:
        model = Team
        fields = ('name', 'slug', 'logo', 'city', 'stadium',
                  'established_date', 'website', 'league')


class HonorFrontListSerializer(serializers.ModelSerializer):
    team = serializers.CharField(source='team.name', read_only=True)
    class Meta:
        model = Honor
        fields = ('title', 'slug', 'year', 'description',
                  'level', 'team')