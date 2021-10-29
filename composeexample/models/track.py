from django.db import models

from composeexample.models.album import Album


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    length = models.IntegerField()
