from django.db import models

# Create your models here.


class League(models.Model):
    class ContinentTextChoice(models.TextChoices):
        ASIA = 'Asia'
        EUROPEAN = 'European'
        OCEANIA = 'Oceania'
        NORTH_AMERICA = 'North America'
        SOUTH_AMERICA = 'South America'
        AFRICA = 'Africa'
    name = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    logo = models.ImageField(blank=True, upload_to='images/logo')
    country = models.CharField(max_length=64)
    continent = models.CharField(max_length=13, choices=ContinentTextChoice.choices,
                                 default=ContinentTextChoice.EUROPEAN)
    established_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    website = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['country']),
        ]
        verbose_name = 'league'
        verbose_name_plural = 'leagues'