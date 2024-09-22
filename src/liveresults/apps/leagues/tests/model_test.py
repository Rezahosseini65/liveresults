from django.test import TestCase

from liveresults.apps.leagues.models import League


class LeagueModelTest(TestCase):
    def setUp(self):
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

    def test_league_model(self):
        self.assertEqual(self.league.name, 'Premier League')
        self.assertEqual(self.league.slug, 'premier-league')
        self.assertEqual(self.league.country, 'England')
        self.assertEqual(self.league.continent, League.ContinentTextChoice.EUROPEAN)
        self.assertEqual(self.league.established_date, '1920-02-20')
        self.assertEqual(self.league.description, 'Top level English football league')
        self.assertTrue(self.league.is_active)
        self.assertEqual(self.league.website, 'https://www.premierleague.com')


    def test_str_method(self):
        self.assertEqual(str(self.league.name), 'Premier League')
        