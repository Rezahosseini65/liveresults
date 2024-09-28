from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from liveresults.apps.leagues.models import League
from liveresults.apps.teams.models import Team


class TeamFrontViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.league = League.objects.create(name='Premier League')
        self.team = Team.objects.create(
            league=self.league,
            name='Team',
            slug='team',
            city='city test',
            established_date = '1980-02-02'
        )

    def test_team_get(self):
        url = reverse('front-team:team-front-retrieve', args=[self.team.name])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['league'], 'Premier League')
        self.assertEqual(response.data['name'], 'Team')
        self.assertEqual(response.data['slug'], 'team')
        self.assertEqual(response.data['city'], 'city test')
        self.assertEqual(response.data['established_date'], '1980-02-02')
