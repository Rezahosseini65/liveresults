from django.urls import path

from liveresults.apps.teams.views.admin import TeamAdminCreateView, TeamAdminRetrieveView

urlpatterns = [
    path('create/', TeamAdminCreateView.as_view(), name='create-team'),
    path('retrieve/<str:name>/', TeamAdminRetrieveView.as_view(), name='retrieveView'),
]