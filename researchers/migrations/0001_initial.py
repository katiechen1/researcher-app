# Generated by Django 2.0.2 on 2018-03-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('website_link', models.CharField(max_length=200)),
                ('linkedin_link', models.CharField(max_length=200)),
                ('levels', models.CharField(choices=[('S', 'Senior'), ('J', 'Junior')], max_length=1)),
            ],
        ),
    ]
