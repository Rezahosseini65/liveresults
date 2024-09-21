from rest_framework import serializers

from liveresults.apps.leagues.models import League


class LeagueFrontListSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('name', 'slug', 'logo')


class LeagueFrontDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'