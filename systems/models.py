from django.db import models
from django.contrib.auth.models import User
from products.models import *
# Create your models here.

class FuelLogSystemOneMod(models.Model):
    products = tuple(productsMod.objects.values_list('id', 'product_type'))
    buckets_added = models.FloatField()
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    thumb = models.ImageField(blank=True,null=True)
    product = models.IntegerField(choices=products,default=0)
    def __str__(self):
        return str(self.id) + " " + str(self.day) + " "  + str(self.staff)

class monthlyMeterSystemOneMod(models.Model):
    system = models.CharField(max_length=50,default='6000100118')
    serial_number = models.CharField(max_length=50,default='80003356')
    current_meter_reading = models.IntegerField(default=0)
    previous_meter_reading = models.IntegerField(default=0)
    difference = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " " + str(self.serial_number)

class FuelLogSystemTwoMod(models.Model):
    buckets_added = models.DecimalField(max_digits=1000,decimal_places=1)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    thumb = models.ImageField(blank=True,null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " "  + str(self.staff)

class monthlyMeterSystemTwoMod(models.Model):
    system = models.CharField(max_length=50,default='6000150218')
    serial_number = models.CharField(max_length=50,default='80003384')
    current_meter_reading = models.IntegerField(default=0)
    previous_meter_reading = models.IntegerField(default=0)
    difference = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " " + str(self.serial_number)

class FuelLogSystemThreeMod(models.Model):
    buckets_added = models.DecimalField(max_digits=1000,decimal_places=1)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    thumb = models.ImageField(blank=True,null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " "  + str(self.staff)

class monthlyMeterSystemThreeMod(models.Model):
    system = models.CharField(max_length=50,default='6000140218')
    serial_number = models.CharField(max_length=50,default='80003353')
    current_meter_reading = models.IntegerField(default=0)
    previous_meter_reading = models.IntegerField(default=0)
    difference = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " " + str(self.serial_number)

class FuelLogSystemFourMod(models.Model):
    buckets_added = models.DecimalField(max_digits=1000,decimal_places=1)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    thumb = models.ImageField(blank=True,null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " "  + str(self.staff)

class monthlyMeterSystemFourMod(models.Model):
    system = models.CharField(max_length=50,default='6000170218')
    serial_number = models.CharField(max_length=50,default='80003374')
    current_meter_reading = models.IntegerField(default=0)
    previous_meter_reading = models.IntegerField(default=0)
    difference = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " " + str(self.serial_number)

class FuelLogSystemFiveMod(models.Model):
    buckets_added = models.DecimalField(max_digits=1000,decimal_places=1)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    thumb = models.ImageField(blank=True,null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " "  + str(self.staff)

class monthlyMeterSystemFiveMod(models.Model):
    system = models.CharField(max_length=50,default='6000160218')
    serial_number = models.CharField(max_length=50,default='80003359')
    current_meter_reading = models.IntegerField(default=0)
    previous_meter_reading = models.IntegerField(default=0)
    difference = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " " + str(self.serial_number)

class FuelLogSystemSixMod(models.Model):
    buckets_added = models.DecimalField(max_digits=1000,decimal_places=1)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    thumb = models.ImageField(blank=True,null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " "  + str(self.staff)

class monthlyMeterSystemSixMod(models.Model):
    system = models.CharField(max_length=50,default='6000200318')
    serial_number = models.CharField(max_length=50,default='80003366')
    current_meter_reading = models.IntegerField(default=0)
    previous_meter_reading = models.IntegerField(default=0)
    difference = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " " + str(self.serial_number)

class FuelLogSystemSevenMod(models.Model):
    buckets_added = models.DecimalField(max_digits=1000,decimal_places=1)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    thumb = models.ImageField(blank=True,null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " "  + str(self.staff)

class monthlyMeterSystemSevenMod(models.Model):
    system = models.CharField(max_length=50,default='6000190318')
    serial_number = models.CharField(max_length=50,default='80003368')
    current_meter_reading = models.IntegerField(default=0)
    previous_meter_reading = models.IntegerField(default=0)
    difference = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " " + str(self.serial_number)


class FuelLogSystemEightMod(models.Model):
    buckets_added = models.DecimalField(max_digits=1000,decimal_places=1)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    thumb = models.ImageField(blank=True,null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " "  + str(self.staff)

class monthlyMeterSystemEightMod(models.Model):
    system = models.CharField(max_length=50,default='6000240318')
    serial_number = models.CharField(max_length=50,default='80059986')
    current_meter_reading = models.IntegerField(default=0)
    previous_meter_reading = models.IntegerField(default=0)
    difference = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " " + str(self.serial_number)


class FuelLogSystemNineMod(models.Model):
    buckets_added = models.DecimalField(max_digits=1000,decimal_places=1)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    thumb = models.ImageField(blank=True,null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " "  + str(self.staff)

class monthlyMeterSystemNineMod(models.Model):
    system = models.CharField(max_length=50,default='6000210318')
    serial_number = models.CharField(max_length=50,default='80059970')
    current_meter_reading = models.IntegerField(default=0)
    previous_meter_reading = models.IntegerField(default=0)
    difference = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " " + str(self.serial_number)

class FuelLogSystemTenMod(models.Model):
    buckets_added = models.DecimalField(max_digits=1000,decimal_places=1)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    thumb = models.ImageField(blank=True,null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " "  + str(self.staff)

class monthlyMeterSystemTenMod(models.Model):
    system = models.CharField(max_length=50,default='6000220318')
    serial_number = models.CharField(max_length=50,default='80059988')
    current_meter_reading = models.IntegerField(default=0)
    previous_meter_reading = models.IntegerField(default=0)
    difference = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)
    day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " " + str(self.serial_number)
