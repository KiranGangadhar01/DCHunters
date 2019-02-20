# Generated by Django 2.1.4 on 2019-02-15 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playerstats', '0007_remove_player_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='Likes',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='Mostkills',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='Season02_Headshot',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='Season02_Kills',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='Season03_Headshot',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='Season03_Kills',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='Season04_Headshot',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='Season04_Kills',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='Season05_Headshot',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='Season05_Kills',
            field=models.IntegerField(default=1),
        ),
    ]
