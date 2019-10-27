from django.contrib import admin

from .models import Researcher

from django.utils.encoding import smart_str

import csv
from django.http import HttpResponse

def export_csv(modeladmin, request, queryset):
   
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"First Name"),
        smart_str(u"Last Name"),
        smart_str(u"Full Name"),
        smart_str(u"Email"),
        smart_str(u"Institution Name"),
        smart_str(u"Position"),
        smart_str(u"Country"),
        smart_str(u"Website Link"),
        smart_str(u"Level"),
        smart_str(u"Description"),
            ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.firstname),
            smart_str(obj.lastname),
            smart_str(obj.fullname),
            smart_str(obj.email),
            smart_str(obj.institution),
            smart_str(obj.position),
            smart_str(obj.country),
            smart_str(obj.website_link),
            smart_str(obj.level),
            smart_str(obj.des),
            ])
    return response
export_csv.short_description = u"Export CSV"


@admin.register(Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'institution', 'position', 'country', 'website_link', 'level']
    search_fields = ['firstname', 'lastname', 'institution', 'position', 'country', 'website_link', 'level']
    actions=[export_csv]
