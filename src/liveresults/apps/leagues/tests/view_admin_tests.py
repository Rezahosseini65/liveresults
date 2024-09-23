from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from liveresults.apps.leagues.models import League
from liveresults.apps.leagues.serializers.admin import LeagueAdminSerializer


class LeagueAdminViewTest(APITestCase):
    league_data = None

    @classmethod
    def setUpTestData(cls):
        cls.league_data = {'name':'Test League',
                            'slug':'test-league',
                            'country':'Test Country',
                            'continent': League.ContinentTextChoice.EUROPEAN,
                            'established_date':'1920-02-20',
                            'is_active':True,
                            'website':'https://www.premierleague.com'
                            }
        cls.league, created = League.objects.update_or_create(
            slug=cls.league_data['slug'], defaults=cls.league_data
        )
        cls.url = reverse('admin-league:league-admin')

    def test_create_league(self):
        new_league_data = self.league_data.copy()
        new_league_data['slug'] = 'new-test-league'
        response = self.client.post(self.url, new_league_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(League.objects.count(), 2)
        self.assertEqual(response.data['name'], new_league_data['name'])

    def test_get_league_list(self):
        response = self.client.get(self.url, format = 'json')
        leagues = League.objects.all()
        serializer = LeagueAdminSerializer(leagues, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_league(self):
        update_data = {'name': 'Update Name', 'country': 'Update Country'}
        url = reverse('admin-league:league-detail', kwargs={'pk': self.league.pk})
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.league.refresh_from_db()
        self.assertEqual(self.league.name, update_data['name'])

    def test_delete_league(self):
        url = reverse('admin-league:league-detail', kwargs={'pk': self.league.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(League.objects.count(), 0)