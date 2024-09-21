from django.urls import path

from liveresults.apps.leagues.views.admin import LeagueAdminView

urlpatterns = [
    path('', LeagueAdminView.as_view(), name='league-admin'),
]