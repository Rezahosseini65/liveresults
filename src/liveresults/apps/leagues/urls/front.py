from django.urls import path

from liveresults.apps.leagues.views.front import LeagueFrontListView, LeagueFrontDetailView

urlpatterns = [
    path('', LeagueFrontListView.as_view(), name='league-list'),
    path('<int:pk>/', LeagueFrontDetailView.as_view(), name='league-detail'),
]