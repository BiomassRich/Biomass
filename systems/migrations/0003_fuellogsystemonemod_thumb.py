# Generated by Django 2.2.4 on 2020-03-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0002_fuellogsystemeightmod_fuellogsystemfivemod_fuellogsystemfourmod_fuellogsystemninemod_fuellogsystemse'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuellogsystemonemod',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
