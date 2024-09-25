from django.urls import path

from liveresults.apps.teams.views.front import TeamFrontRetrieveView

urlpatterns = [
    path('retrieve/<str:name>/', TeamFrontRetrieveView.as_view(), name='team-front-retrieve'),
]