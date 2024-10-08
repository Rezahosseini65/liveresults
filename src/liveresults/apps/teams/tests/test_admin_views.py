from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from liveresults.apps.leagues.models import League
from liveresults.apps.teams.models import Team, Honor


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


class HonorAdminTest(APITestCase):
    def setUp(self):
        self.league = League.objects.create(name='Premier League')
        self.team = Team.objects.create(
            league=self.league,
            name='Test Team',
            slug='test-team',
            city='Test City',
            established_date='2000-01-01'
        )
        self.honor = Honor.objects.create(
            team=self.team,
            title='Honor Test',
            slug='honor-test',
            year='2024-02-02',
            description='description honor test',
            level=Honor.LevelTextChoice.DOMESTIC

        )

    def test_create_honor(self):
        url = reverse('admin-team:create-honor')
        data = {
            'team':self.team.name,
            'title':'New Honor',
            'slug':'new-honor',
            'year':'2024-01-01',
            'description':'new honor description'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_honor(self):
        url = reverse('admin-team:detail-honor', args=[self.honor.pk])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Honor Test')

    def test_update_honor(self):
        url = reverse('admin-team:detail-honor', args=[self.honor.pk])
        data = {
            'team':self.team.name,
            'title':'Update Honor',
            'slug':'update-honor',
            'year':'2024-03-03',
            'description':'update description'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.honor.refresh_from_db()
        self.assertEqual(self.honor.title, 'Update Honor')

    def test_delete_honor(self):
        url = reverse('admin-team:detail-honor', args=[self.honor.pk])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Honor.objects.count(), 0)