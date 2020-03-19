from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'fuelrecords'

urlpatterns = [
    path('fuelrecordlog',views.FuelDeliveryLog, name='fuelrecord'),
    path('viewfuelrecordlog',views.ViewFuelDeliverylog, name='viewfuelrecord'),
    path('<id>/',views.FuelDeliveryRecords, name='idRecord'),
]
