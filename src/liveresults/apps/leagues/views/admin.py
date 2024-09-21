from rest_framework import generics
from rest_framework.permissions import AllowAny

from liveresults.apps.leagues.models import League
from liveresults.apps.leagues.serializers.admin import LeagueAdminSerializer


class LeagueAdminView(generics.ListCreateAPIView,
                      generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueAdminSerializer
    permission_classes = [AllowAny]
