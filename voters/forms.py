from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *

class Voter(forms.Form):
     
    first_name = forms.CharField(max_length = 200)
    ID_number = forms.IntegerField(
                     help_text = "Enter 10 digit id number"
                     )
    location_name = forms.CharField(max_length = 200)
    password = forms.CharField(widget = forms.PasswordInput())