from rest_framework import serializers

from liveresults.apps.teams.models import Team
from liveresults.apps.leagues.models import League


class TeamAdminCreateSerializer(serializers.ModelSerializer):
    league = serializers.CharField(source='league.name')

    class Meta:
        model = Team
        fields = ('name', 'slug', 'logo', 'city', 'stadium',
                  'established_date', 'website', 'league')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['league'] = instance.league.name
        return representation

    def to_internal_value(self, data):
        league_name = data.get('league')
        try:
            league = League.objects.get(name=league_name)
        except League.DoesNotExist:
            raise serializers.ValidationError({'league':'League not found'})

        validated_data = super().to_internal_value(data)
        validated_data['league'] = league
        return validated_data

    def create(self, validated_data):
        league = validated_data.pop('league')
        team = Team.objects.create(league=league, **validated_data)
        return team


class TeamAdminRetrieveSerializer(serializers.ModelSerializer):
    league = serializers.CharField(source='league.name', read_only=True)

    class Meta:
        model = Team
        fields = ('name', 'slug', 'logo', 'city', 'stadium',
                  'established_date', 'website', 'league')