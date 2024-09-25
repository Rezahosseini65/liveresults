from django.db import models

from liveresults.apps.leagues.models import League
from liveresults.apps.teams.validators import validate_png


# Create your models here.


class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.PROTECT, related_name='teams')
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, allow_unicode=True)
    logo = models.ImageField(blank=True, upload_to='images/teams/logos/', validators=[validate_png])
    city = models.CharField(max_length=128)
    stadium = models.CharField(max_length=128, blank=True)
    established_date = models.DateField(blank=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['city'])
        ]
        verbose_name = 'team'
        verbose_name_plural = 'teams'

    def __str__(self):
        return self.name

    @property
    def league_name(self):
        return self.league.name


class Honor(models.Model):
    class LevelTextChoice(models.TextChoices):
        DOMESTIC = 'Domestic'
        INTERNATIONAL = 'International'
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='honors')
    title = models.CharField(max_length=128)
    slug = models.SlugField(blank=True, allow_unicode=True)
    year = models.DateField()
    description = models.TextField(blank=True)
    level = models.CharField(max_length=13, choices=LevelTextChoice.choices,
                             default=LevelTextChoice.DOMESTIC)

    class Meta:
        ordering = ['year']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['year']),
            models.Index(fields=['level'])
        ]

        verbose_name = 'honor'
        verbose_name_plural = 'honors'

    def __str__(self):
        return f'{self.team.name}--{self.title}'


