# Generated by Django 2.2.7 on 2020-03-06 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('systems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='monthlyMeterSystemTwoMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(default='6000150218', max_length=50)),
                ('serial_number', models.CharField(default='80003384', max_length=50)),
                ('current_meter_reading', models.IntegerField(default=0)),
                ('previous_meter_reading', models.IntegerField(default=0)),
                ('difference', models.IntegerField(null=True)),
                ('notes', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='monthlyMeterSystemThreeMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(default='6000140218', max_length=50)),
                ('serial_number', models.CharField(default='80003353', max_length=50)),
                ('current_meter_reading', models.IntegerField(default=0)),
                ('previous_meter_reading', models.IntegerField(default=0)),
                ('difference', models.IntegerField(null=True)),
                ('notes', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='monthlyMeterSystemTenMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(default='6000220318', max_length=50)),
                ('serial_number', models.CharField(default='80059988', max_length=50)),
                ('current_meter_reading', models.IntegerField(default=0)),
                ('previous_meter_reading', models.IntegerField(default=0)),
                ('difference', models.IntegerField(null=True)),
                ('notes', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='monthlyMeterSystemSixMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(default='6000200318', max_length=50)),
                ('serial_number', models.CharField(default='80003366', max_length=50)),
                ('current_meter_reading', models.IntegerField(default=0)),
                ('previous_meter_reading', models.IntegerField(default=0)),
                ('difference', models.IntegerField(null=True)),
                ('notes', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='monthlyMeterSystemSevenMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(default='6000190318', max_length=50)),
                ('serial_number', models.CharField(default='80003368', max_length=50)),
                ('current_meter_reading', models.IntegerField(default=0)),
                ('previous_meter_reading', models.IntegerField(default=0)),
                ('difference', models.IntegerField(null=True)),
                ('notes', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='monthlyMeterSystemNineMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(default='6000210318', max_length=50)),
                ('serial_number', models.CharField(default='80059970', max_length=50)),
                ('current_meter_reading', models.IntegerField(default=0)),
                ('previous_meter_reading', models.IntegerField(default=0)),
                ('difference', models.IntegerField(null=True)),
                ('notes', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='monthlyMeterSystemFourMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(default='6000170218', max_length=50)),
                ('serial_number', models.CharField(default='80003374', max_length=50)),
                ('current_meter_reading', models.IntegerField(default=0)),
                ('previous_meter_reading', models.IntegerField(default=0)),
                ('difference', models.IntegerField(null=True)),
                ('notes', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='monthlyMeterSystemFiveMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(default='6000160218', max_length=50)),
                ('serial_number', models.CharField(default='80003359', max_length=50)),
                ('current_meter_reading', models.IntegerField(default=0)),
                ('previous_meter_reading', models.IntegerField(default=0)),
                ('difference', models.IntegerField(null=True)),
                ('notes', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='monthlyMeterSystemEightMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(default='6000240318', max_length=50)),
                ('serial_number', models.CharField(default='80059986', max_length=50)),
                ('current_meter_reading', models.IntegerField(default=0)),
                ('previous_meter_reading', models.IntegerField(default=0)),
                ('difference', models.IntegerField(null=True)),
                ('notes', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FuelLogSystemTwoMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buckets_added', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FuelLogSystemThreeMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buckets_added', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FuelLogSystemTenMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buckets_added', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FuelLogSystemSixMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buckets_added', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FuelLogSystemSevenMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buckets_added', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FuelLogSystemNineMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buckets_added', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FuelLogSystemFourMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buckets_added', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FuelLogSystemFiveMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buckets_added', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FuelLogSystemEightMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buckets_added', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
