from django.urls import path

from liveresults.apps.leagues.views.admin import LeagueAdminListView, LeagueAdminDetailView

urlpatterns = [
    path('', LeagueAdminListView.as_view(), name='league-admin'),
    path('<int:pk>/', LeagueAdminDetailView.as_view(), name='league-detail'),
]
