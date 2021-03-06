from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import related


class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # save location
    def save_location(self):
        self.save()

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=30)
    

    # save location
    def save_gender(self):
        self.save()

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)   
    username =  models.CharField(max_length=100)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=250)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def create_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    def _str_(self):
        return self.user.username
    
class Votes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True) 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    id_number = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE,null=True)
    voters_image = CloudinaryField("image",null=True, blank=True)
    
    def save_Votes(self):
        self.save()
        
    def __str__(self):
        return self.location
