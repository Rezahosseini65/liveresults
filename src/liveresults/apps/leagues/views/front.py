from rest_framework import generics
from rest_framework.permissions import AllowAny

from liveresults.apps.leagues.models import League
from liveresults.apps.leagues.serializers.front import LeagueFrontListSerializer, LeagueFrontDetailSerializer


class LeagueFrontListView(generics.ListAPIView):
    queryset = League.objects.all().only('name', 'slug', 'logo')
    serializer_class = LeagueFrontListSerializer
    permission_classes = [AllowAny]

class LeagueFrontDetailView(generics.RetrieveAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueFrontDetailSerializer
    permission_classes = [AllowAny]