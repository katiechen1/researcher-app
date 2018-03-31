from django.db import models
from django import forms
from django.contrib.auth.models import User 

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        # fields = ['username', 'password', 'your_email', 'your_website', 'your_institution', 'your_description']
        fields = ['username', 'password']