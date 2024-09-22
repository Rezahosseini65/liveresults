from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from liveresults.apps.leagues.models import League


class LeagueFrontListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        League.objects.create(name='League 1', slug='league-1', logo='logo1.png')
        League.objects.create(name='League 2', slug='league-2', logo='logo2.png')

    def test_league_list(self):
        url = reverse('front-league:league-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'League 1')
        self.assertEqual(response.data[1]['name'], 'League 2')


class LeagueFrontDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.league = League.objects.create(
            name='Premier League',
            slug='premier-league',
            country='England',
            continent=League.ContinentTextChoice.EUROPEAN,
            established_date='1920-02-20',
            description='Top level English football league',
            is_active=True,
            website='https://www.premierleague.com'
        )

    def test_league_detail(self):
        url = reverse('front-league:league-detail', args=[self.league.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Premier League')
        self.assertEqual(response.data['slug'], 'premier-league')
        self.assertEqual(response.data['country'], 'England')
        self.assertEqual(response.data['continent'], League.ContinentTextChoice.EUROPEAN)
        self.assertEqual(response.data['established_date'], '1920-02-20')
        self.assertEqual(response.data['description'],
                         'Top level English football league')
        self.assertTrue(response.data['is_active'],)
        self.assertEqual(response.data['website'], 'https://www.premierleague.com')
