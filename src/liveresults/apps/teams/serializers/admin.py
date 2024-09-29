from rest_framework import serializers

from liveresults.apps.teams.models import Team, Honor
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


class HonorAdminCreateSerializer(serializers.ModelSerializer):
    team = serializers.CharField(source='team.name')
    class Meta:
        model = Honor
        fields = ('title', 'slug', 'year', 'description',
                  'level', 'team')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['team'] = instance.team.name
        return representation

    def to_internal_value(self, data):
        team_name = data.get('team')
        try:
            team = Team.objects.get(name=team_name)
        except Team.DoesNotExist:
            raise serializers.ValidationError({'team': 'team not found'})

        validated_data = super().to_internal_value(data)
        validated_data['team'] = team
        return validated_data

    def create(self, validated_data):
        team = validated_data.pop('team')
        honor = Honor.objects.create(team=team, **validated_data)
        return honor


class HonorAdminRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):
    team = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = Honor
        fields = ('title', 'slug', 'year', 'description',
                  'level', 'team')
