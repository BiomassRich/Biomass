from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class productsMod(models.Model):
    product_type = models.CharField(max_length=50)
    product_size = models.CharField(max_length=50)
    source_supplier = models.CharField(max_length=50)
    stock = models.IntegerField()
    entry_date = models.DateTimeField(auto_now_add = True)
    entry_day = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.product_type) + " "  + str(self.staff)
