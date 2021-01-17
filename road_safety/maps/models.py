from django.db import models

class Accidents(models.Model):
    lat = models.CharField(max_length=30)
    long = models.CharField(max_length=30)
    street = models.CharField(max_length=100)
    zip = models.IntegerField()
    
class Scores(models.Model):
    score = models.FloatField()
    street = models.CharField(max_length=100)
    zip = models.IntegerField()