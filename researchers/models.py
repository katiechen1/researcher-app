from django.db import models
from django import forms
from django.contrib.auth.models import User 
from django.utils import timezone
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

#Researcher objects for each researcher on the page 
class Researcher(models.Model):
    LEVELS_CHOICES = [('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Full Professor', 'Full Professor'), ('Senior Industry Scientist', 'Senior Industry Scientist')]
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    website_link = models.CharField(max_length=200)
    linkedin_link = models.CharField(max_length=200)
    level = models.CharField(choices=LEVELS_CHOICES, blank=True, max_length=200)
    des = models.CharField(max_length=200)

class FeedbackForm(forms.Form):
    feedback = forms.CharField(required=True,
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}), max_length=200)

# This is the form used to nominvi modeate a scholar or yourself
class NominateForm(forms.Form):
    nominators_full_name = forms.CharField(required=True)
    nominators_email = forms.EmailField(required=True)
    nominees_name = forms.CharField(required=True)
    nominees_email = forms.EmailField(required=True)

# This is the form we send to nominated individual to get information needed to display
class NominatedInfo(forms.Form):
    LEVELS_CHOICES = [('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Full Professor', 'Full Professor'), ('Senior Industry Scientist', 'Senior Industry Scientist')]
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    institution = forms.CharField(required=True)
    position = forms.CharField(required=True)
    website = forms.CharField(required=False)
    country = forms.CharField(required=True)
    level = forms.ChoiceField(choices=LEVELS_CHOICES, required=True)
    description = forms.CharField(required=True,
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}), max_length=200)
    class Meta:
        model = Researcher

# #checking that keyword is at least five words
# def mfive(value):
#     if len(value) < 5:
#         raise ValidationError(
#             _('%(value)s is not at least five words'),
#             params={'value': value},
#         )













