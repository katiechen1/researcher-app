from django.db import models
from django import forms
# Create your models here.

class Researcher(models.Model):
    LEVELS_CHOICES = [('EC', 'Early Career'), ('MS', 'Mid/Senior Career')]
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    website_link = models.CharField(max_length=200)
    linkedin_link = models.CharField(max_length=200)
    level = models.CharField(choices=LEVELS_CHOICES, max_length=200, blank=True)

# This is the form used to nominate a scholar or yourself
class NominateForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    nominee_name = forms.CharField(required=True)
    nominee_email = forms.EmailField(required=True)
    nominee_website = forms.CharField(required=True)
    nominee_institution = forms.CharField(required=True)
    nominee_description = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

# This is the form we send to nominated individual to get information needed to display
class NominatedInfo(forms.Form):
    r_name = forms.CharField(required=True)
    r_short_description = forms.CharField(required=True,
        widget=forms.Textarea)
    r_institution = forms.CharField(required=True)
    r_position = forms.CharField(required=True)
    # country = models.CharField(required=True)
    website_link = forms.CharField(required=True)
    linkedin_link = forms.CharField(required=True)


