from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from liveresults.apps.teams.models import Team, Honor
from liveresults.apps.teams.serializers.admin import (TeamAdminCreateSerializer, TeamAdminRetrieveSerializer, \
    HonorAdminCreateSerializer, HonorAdminRetrieveUpdateDeleteSerializer)


class TeamAdminCreateView(generics.CreateAPIView):
    queryset = Team.objects.all().select_related('league')
    serializer_class = TeamAdminCreateSerializer
    permission_classes = [IsAdminUser]


class TeamAdminRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all().select_related('league')
    serializer_class = TeamAdminRetrieveSerializer
    lookup_field = 'name'
    permission_classes = [IsAdminUser]


class HonorAdminCreateView(generics.CreateAPIView):
    queryset = Honor.objects.all().select_related('team')
    serializer_class = HonorAdminCreateSerializer
    #permission_classes = [IsAdminUser]


class HonorAdminRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Honor.objects.all().select_related('team')
    serializer_class = HonorAdminRetrieveUpdateDeleteSerializer
    #permission_classes = [IsAdminUser]

