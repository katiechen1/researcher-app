from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from researchers.models import Researcher
from pytz import UTC

DATETIME_FORMAT = '%m/%d/%Y %H:%M'

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

class Command(BaseCommand):
	help = "Loads data from researcher_data.csv into Researcher model"

	def handle(self, *args, **options):
		print('inside')
		# if Researcher.object.exists():
		# 	print('Data already loaded, exiting')
		# 	print(ALREADY_LOADED_ERROR_MESSAGE)
		# 	return
		print('Loading researchers from csv file.')
		for row in DictReader(open('./researcher_data.csv')):
			r = Researcher()
			r.firstname = row['firstname']
                        r.lastname = row['lastname']
			r.institution = row['institution']
			r.position = row['position']
			r.country = row['country']
			r.website_link = row['website_link']
			r.level = row['level']
			r.save()
