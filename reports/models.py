from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DatesMod(models.Model):
    fromdate = models.DateField()
    todate = models.DateField()
