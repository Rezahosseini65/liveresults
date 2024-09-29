from django.urls import path

from liveresults.apps.teams.views.front import TeamFrontRetrieveView, HonorFrontListView

urlpatterns = [
    path('retrieve/<str:name>/', TeamFrontRetrieveView.as_view(), name='team-front-retrieve'),
    path('honors/<int:team_id>/', HonorFrontListView.as_view(), name='honor-list'),
]