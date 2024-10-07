from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from liveresults.apps.leagues.models import League
from liveresults.apps.teams.models import Team, Honor


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

        self.honor1 = Honor.objects.create(
            team=self.team,
            title='Honor1 Test',
            slug='honor1-test',
            year='2024-02-02',
            level=Honor.LevelTextChoice.DOMESTIC
        )
        self.honor2 = Honor.objects.create(
            team=self.team,
            title='Honor2 Test',
            slug='honor2-test',
            year='2024-02-02',
            level=Honor.LevelTextChoice.INTERNATIONAL
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

    def test_honor_get(self):
        url = reverse('front-team:honor-list', args=[self.team.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Honor1 Test')
        self.assertEqual(response.data[1]['title'], 'Honor2 Test')