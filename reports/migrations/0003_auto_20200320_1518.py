# Generated by Django 2.2.4 on 2020-03-20 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20200320_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datesmod',
            old_name='becausedate',
            new_name='todate',
        ),
    ]
