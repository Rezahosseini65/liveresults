# Generated by Django 5.1 on 2024-09-21 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='league',
            new_name='leagues_lea_name_1b3d9e_idx',
            old_name='leauges_lea_name_51e5fa_idx',
        ),
        migrations.RenameIndex(
            model_name='league',
            new_name='leagues_lea_country_713330_idx',
            old_name='leauges_lea_country_2bd82c_idx',
        ),
    ]