# Generated by Django 2.1.4 on 2019-02-13 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerstats', '0004_player_totalkills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='TotalKills',
            new_name='TotalWins',
        ),
    ]
