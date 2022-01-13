from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio','contact']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','email']