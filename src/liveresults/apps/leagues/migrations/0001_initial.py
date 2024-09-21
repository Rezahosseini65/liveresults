# Generated by Django 5.1 on 2024-09-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=128)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('logo', models.ImageField(blank=True, upload_to='images/logo')),
                ('country', models.CharField(max_length=64)),
                ('continent', models.CharField(choices=[('Asia', 'Asia'), ('European', 'European'), ('Oceania', 'Oceania'), ('North America', 'North America'), ('South America', 'South America'), ('Africa', 'Africa')], default='European', max_length=13)),
                ('established_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('website', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'league',
                'verbose_name_plural': 'leagues',
                'indexes': [models.Index(fields=['name'], name='leauges_lea_name_51e5fa_idx'), models.Index(fields=['country'], name='leauges_lea_country_2bd82c_idx')],
            },
        ),
    ]
