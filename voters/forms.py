from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        fields=['username',  'profile_pic', 'bio', 'location', ]


class VotersForm(forms.ModelForm):
    class Meta:
        model= Votes      
        fields=['id_number',  'voters_image', 'location','gender' ]