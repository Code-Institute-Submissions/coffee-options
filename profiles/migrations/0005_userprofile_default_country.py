# Generated by Django 3.1.3 on 2020-11-28 22:48

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userprofile_default_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
