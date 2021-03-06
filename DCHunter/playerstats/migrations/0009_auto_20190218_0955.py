# Generated by Django 2.1.4 on 2019-02-18 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playerstats', '0008_auto_20190215_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Killratio',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='Season02_Matches',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='Season03_Matches',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='Season04_Matches',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='Season05_Matches',
            field=models.IntegerField(default=1),
        ),
    ]
