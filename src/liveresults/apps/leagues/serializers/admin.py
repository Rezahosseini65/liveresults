from rest_framework import serializers

from liveresults.apps.leagues.models import League


class LeagueAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('name', 'slug', 'logo', 'country', 'continent',
                  'established_date', 'description', 'is_active', 'website')
