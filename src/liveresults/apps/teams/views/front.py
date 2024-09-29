from rest_framework import generics
from rest_framework.permissions import AllowAny

from liveresults.apps.teams.models import Team, Honor
from liveresults.apps.teams.serializers.front import TeamFrontRetrieveSerializer, HonorFrontListSerializer


class TeamFrontRetrieveView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamFrontRetrieveSerializer
    lookup_field = 'name'
    permission_classes = [AllowAny]


class HonorFrontListView(generics.ListAPIView):
    serializer_class = HonorFrontListSerializer

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        return Honor.objects.filter(team_id=team_id).select_related('team')