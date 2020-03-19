from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .models import *

# Create your views here.
@login_required(login_url="/accounts/login/")
def FuelDeliveryLog(request):
    entriesLog = FuelLogDeliveryMod.objects.all().order_by('entry_date')
    if request.method == 'POST':
        form = forms.FuelLogDeliveryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.FuelLogDeliveryForm()
    return render(request,'fueldelivery/fuelrecord.html',{'form':form,'entriesLog':entriesLog})

@login_required(login_url="/accounts/login/")
def ViewFuelDeliverylog(request):
    entriesLog = FuelLogDeliveryMod.objects.all().order_by('entry_date')
    return render(request,'fueldelivery/viewfuelrecord.html',{'entriesLog':entriesLog})

@login_required(login_url="/accounts/login/")
def FuelDeliveryRecords(request,id):
    id = FuelLogDeliveryMod.objects.get(id=id)
    return render(request,'fueldelivery/idrecord.html',{'id':id})
