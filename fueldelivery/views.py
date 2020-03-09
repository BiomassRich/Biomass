from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .models import *

# Create your views here.
@login_required(login_url="/accounts/login/")
def FuelDeliveryLog(request):
    entries = FuelLogDeliveryMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.FuelLogDeliveryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.FuelLogDeliveryForm()
    return render(request,'fueldelivery/fuelrecord.html',{'form':form,'entry':entries})
