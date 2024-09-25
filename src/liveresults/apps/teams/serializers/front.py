from rest_framework import serializers

from liveresults.apps.teams.models import Team


class TeamFrontRetrieveSerializer(serializers.ModelSerializer):
    league = serializers.CharField(source='league.name')

    class Meta:
        model = Team
        fields = ('name', 'slug', 'logo', 'city', 'stadium',
                  'established_date', 'website', 'league')