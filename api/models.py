from pyexpat import model
from statistics import mode
from turtle import width
from django.db import models

# Create your models here.


class meme(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()
    box_count = models.IntegerField()
