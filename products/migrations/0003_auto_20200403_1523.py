# Generated by Django 2.2.7 on 2020-04-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productsmod_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmod',
            name='stock',
            field=models.DecimalField(decimal_places=1, max_digits=1000),
        ),
    ]
