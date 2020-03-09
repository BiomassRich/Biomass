from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FuelLogDeliveryMod(models.Model):
    delivery_ref_number = models.CharField(max_length=50)
    type_of_biomass = models.CharField(max_length=50)
    description_moisture_content = models.CharField(max_length=50)
    source_supplier = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    BSL_Number = models.IntegerField()
    delivery_note_number = models.IntegerField()
    delivery_date = models.DateTimeField()
    entry_date = models.DateTimeField(auto_now_add = True)
    entry_day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.day) + " "  + str(self.staff)
