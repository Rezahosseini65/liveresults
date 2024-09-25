from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from liveresults.apps.teams.models import Team
from liveresults.apps.teams.serializers.admin import TeamAdminCreateSerializer, TeamAdminRetrieveSerializer


class TeamAdminCreateView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamAdminCreateSerializer
    permission_classes = [IsAdminUser]


class TeamAdminRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamAdminRetrieveSerializer
    lookup_field = 'name'
    permission_classes = [IsAdminUser]
