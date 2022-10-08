import django.utils.timezone
from django.db import models


# Create your models here.
# Artiste, Song, Lyric
# Model: Artiste, Song, Lyric
# Attributes for “Artiste” : first_name, last_name, age
# Attributes for “Song” : title, date released, likes, artiste_id
# Attributes for “Lyric”: content, song_id


class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()


class Song(models.Model):
    # ForeignKey attribute for specifying many-to-one relationship
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateField(default=django.utils.timezone.now())
    likes = models.IntegerField()
    artiste_id = models.CharField(max_length=10)


class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
    song_id = models.IntegerField()
