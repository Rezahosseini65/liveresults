from django.test import TestCase

from liveresults.apps.leagues.models import League
from liveresults.apps.teams.models import Team, Honor


class TeamModelTest(TestCase):
    def setUp(self):
        self.league = League.objects.create(name='Premier League')

        self.team = Team.objects.create(
            league= self.league,
            name= 'Manchester City',
            slug= 'manchester-city',
            logo= 'logo.png',
            city = 'manchester',
            stadium='City',
            established_date='1880-02-20',
            website='https://www.mancity.com'

        )

        self.honor = Honor.objects.create(
            team = self.team,
            title = 'Title Test',
            slug = 'title-test',
            year = '2024-02-02',
            description = 'description test',
            level = Honor.LevelTextChoice.DOMESTIC
        )


    def test_team_model(self):
        self.assertEqual(self.team.league, self.league)
        self.assertEqual(self.team.name, 'Manchester City')
        self.assertEqual(self.team.slug, 'manchester-city')
        self.assertEqual(self.team.logo, 'logo.png')
        self.assertEqual(self.team.city, 'manchester')
        self.assertEqual(self.team.stadium, 'City')
        self.assertEqual(self.team.established_date, '1880-02-20')
        self.assertEqual(self.team.website, 'https://www.mancity.com')


    def test_team_str_method(self):
        self.assertEqual(str(self.team.name), 'Manchester City')


    def test_honor_model(self):
        self.assertEqual(self.honor.team, self.team)
        self.assertEqual(self.honor.title, 'Title Test')
        self.assertEqual(self.honor.slug, 'title-test')
        self.assertEqual(self.honor.year, '2024-02-02')
        self.assertEqual(self.honor.description, 'description test')
        self.assertEqual(self.honor.level, Honor.LevelTextChoice.DOMESTIC)


    def test_honor_str_method(self):
        expected_str = f'{self.team.name}--{self.honor.title}'
        self.assertEqual(str(self.honor), expected_str)