from django.db import models

# Create your models here.


class Meme(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()
    box_count = models.IntegerField()

    def __str__(self):
        return self.id
