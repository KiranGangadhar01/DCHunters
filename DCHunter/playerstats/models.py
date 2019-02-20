from django.db import models

# Create your models here.
class Player(models.Model):
    PlayerName = models.CharField(max_length=128, unique=True)
    Likes = models.IntegerField(default=1)

    Season02_Matches = models.IntegerField(default=1)
    Season02_Wins = models.IntegerField()
    Season02_Kills = models.IntegerField(default=1)
    Season02_Headshot = models.IntegerField(default=1)

    Season03_Matches = models.IntegerField(default=1)
    Season03_Wins = models.IntegerField()
    Season03_Kills = models.IntegerField(default=1)
    Season03_Headshot = models.IntegerField(default=1)

    Season04_Matches = models.IntegerField(default=1)
    Season04_Wins = models.IntegerField()
    Season04_Kills = models.IntegerField(default=1)
    Season04_Headshot = models.IntegerField(default=1)

    Season05_Matches = models.IntegerField(default=1)
    Season05_Wins = models.IntegerField()
    Season05_Kills = models.IntegerField(default=1)
    Season05_Headshot = models.IntegerField(default=1)

    Mostkills = models.IntegerField(default=1)

    TotalMatches = models.IntegerField(blank=True, null=True, editable=False)
    TotalWins = models.IntegerField(blank=True, null=True, editable=False)
    TotalKills = models.IntegerField(blank=True, null=True, editable=False)
    TotalHeadshot = models.IntegerField(blank=True, null=True, editable=False)
    Killratio = models.DecimalField(blank=True, null=True, editable=False, max_digits=5, decimal_places=2)
    Headshotratio = models.IntegerField(blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        self.TotalMatches = int(self.Season02_Matches + self.Season03_Matches + self.Season04_Matches + self.Season05_Matches)
        self.TotalWins = int(self.Season02_Wins + self.Season03_Wins + self.Season04_Wins + self.Season05_Wins)
        self.TotalKills = int(self.Season02_Kills + self.Season03_Kills + self.Season04_Kills + self.Season05_Kills)
        self.TotalHeadshot = int(self.Season02_Headshot + self.Season03_Headshot + self.Season04_Headshot + self.Season05_Headshot)
        self.Killratio = (self.TotalKills / self.TotalMatches)
        self.Headshotratio = (self.TotalHeadshot / self.TotalKills) * 100
        super().save(*args, **kwargs)
