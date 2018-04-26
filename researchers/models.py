from django.db import models
from django import forms
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.



#Researcher objects for each researcher on the page 
class Researcher(models.Model):
    LEVELS_CHOICES = [('EC', 'Early Career'), ('MS', 'Mid/Senior Career')]
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    website_link = models.CharField(max_length=200)
    linkedin_link = models.CharField(max_length=200)
    level = models.CharField(choices=LEVELS_CHOICES, max_length=200, blank=True)
    des = models.CharField(max_length=200)

# This is the form used to nominate a scholar or yourself
class NominateForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    nominee_name = forms.CharField(required=True)
    nominee_email = forms.EmailField(required=True)
    nominee_website = forms.CharField(required=True)
    nominee_institution = forms.CharField(required=True)


# This is the form we send to nominated individual to get information needed to display
class NominatedInfo(forms.Form):
    # LEVELS_CHOICES = [('EC', 'Early Career'), ('MS', 'Mid/Senior Career')]
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    institution = forms.CharField(required=True)
    position = forms.CharField(required=True)

    # country = models.CharField(required=True)
    website = forms.CharField(required=True)
    linkedin = forms.CharField(required=True)
    level = forms.CharField(required=True, max_length=2)
    description = forms.CharField(required=True,
        widget=forms.Textarea)
    # level = models.CharField(choices=LEVELS_CHOICES, max_length=200, blank=True)




# one nominator can nominate many researchers
# one to many relationship: foreign key

# #nominator model 
# class Nominator(models.Model):

#     contact_name = forms.CharField(required=True)
#     contact_email = forms.EmailField(required=True)
#     nominee_name = forms.CharField(required=True)
#     nominee_email = forms.EmailField(required=True)
#     nominee_website = forms.CharField(required=True)
#     nominee_institution = forms.CharField(required=True)



# #nominee model
# class Nominee(models.Model):


#     LEVELS_CHOICES = [('EC', 'Early Career'), ('MS', 'Mid/Senior Career')]
    
#     name = forms.CharField(required=True)
#     email = forms.CharField(required=True)
#     institution = forms.CharField(required=True)
#     position = forms.CharField(required=True)
#     description = forms.CharField(required=True,
#         widget=forms.Textarea)
#     website = forms.CharField(required=True)
#     linkedin = forms.CharField(required=True)

#     level = models.CharField(choices=LEVELS_CHOICES, max_length=200, blank=True)

# #nomination model
# class Nomination(models.Model):
#     d_nominator = Nominator()
#     d_nominee = Nominee() 
#     STATUS_CHOICES = [('PENDING', 'pending'), ('APPROVED', 'approved')]
#     nominator = models.ForeignKey(Nominator, on_delete=models.CASCADE)
#     nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
#     status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='PENDING')














