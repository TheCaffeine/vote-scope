from django.db import models

# Create your models here.

class County(models.Model):
    CountyId = models.AutoField(primary_key=True)
    CountyName = models.CharField(max_length=100)

class  Voters(models.Model):
    VoterId = models.AutoField(primary_key=True)
    VoterName = models.CharField(max_length=100)
    County = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)