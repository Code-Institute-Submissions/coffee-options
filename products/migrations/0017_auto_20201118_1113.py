# Generated by Django 3.1.3 on 2020-11-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20201118_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bean',
            name='country_name',
            field=models.CharField(max_length=254),
        ),
    ]
