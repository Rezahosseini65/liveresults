from rest_framework import generics
from rest_framework.permissions import AllowAny

from liveresults.apps.teams.models import Team
from liveresults.apps.teams.serializers.front import TeamFrontRetrieveSerializer


class TeamFrontRetrieveView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamFrontRetrieveSerializer
    lookup_field = 'name'
    permission_classes = [AllowAny]