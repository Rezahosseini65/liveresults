from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from liveresults.apps.leagues.models import League
from liveresults.apps.leagues.serializers.admin import LeagueAdminSerializer


class LeagueAdminListView(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueAdminSerializer
    #permission_classes = [IsAdminUser]



class LeagueAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueAdminSerializer
    #permission_classes = [IsAdminUser]
