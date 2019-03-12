from django.contrib import admin

from .models import Researcher

@admin.register(Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'institution', 'position', 'country', 'website_link', 'linkedin_link', 'level']
    search_fields = ['firstname', 'lastname', 'institution', 'position', 'country', 'website_link', 'linkedin_link', 'level']


