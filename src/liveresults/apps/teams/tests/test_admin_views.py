from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from liveresults.apps.leagues.models import League
from liveresults.apps.teams.models import Team


class TeamAdminViewTest(APITestCase):
    def setUp(self):
        self.league = League.objects.create(name='Premier League')
        self.team = Team.objects.create(
            league=self.league,
            name='Test Team',
            slug='test-team',
            city='Test City',
            established_date='2000-01-01'
        )

    def test_create_team(self):
        url = reverse('admin-team:create-team')
        data = {
            'league': self.league.name,
            'name': 'New Team',
            'slug': 'new-team',
            'city': 'New City',
            'established_date': '2010-05-15'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(Team.objects.get(slug='new-team').name, 'New Team')

    def test_retrieve_team(self):
        url = reverse('admin-team:detail-team', args=[self.team.name])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.team.name)

    def test_update_team(self):
        url = reverse('admin-team:detail-team', args=[self.team.name])
        data = {
            'league': self.league.name,
            'name': 'Updated Team',
            'slug': 'updated-team',
            'city': 'Updated City',
            'established_date': '2001-01-01'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.team.refresh_from_db()
        self.assertEqual(self.team.name, 'Updated Team')

    def test_delete_team(self):
        url = reverse('admin-team:detail-team', args=[self.team.name])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Team.objects.count(), 0)

