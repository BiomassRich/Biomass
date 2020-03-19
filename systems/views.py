from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .models import *

@login_required(login_url="/accounts/login/")
def idfuelLogSystemOne(request,id):
    id = FuelLogSystemOneMod.objects.get(id=id)
    return render(request,'systems/idfuellogsystemone.html',{'id':id})

@login_required(login_url="/accounts/login/")
def idmonthlySystemOne(request,id):
    id = monthlyMeterSystemOneMod.objects.get(id=id)
    return render(request,'systems/idmonthlysystemone.html',{'id':id})

@login_required(login_url="/accounts/login/")
def systemOne(request):
    entriesMonth = monthlyMeterSystemOneMod.objects.all().order_by('date')
    entriesFuel = FuelLogSystemOneMod.objects.all().order_by('date')
    return render(request,'systems/systemone.html',{'entriesMonth':entriesMonth,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemTwo(request):
    entriesMonth = monthlyMeterSystemTwoMod.objects.all().order_by('date')
    entriesFuel = FuelLogSystemTwoMod.objects.all().order_by('date')
    return render(request,'systems/systemtwo.html',{'entriesMonth':entriesMonth,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemThree(request):
    entriesMonth = monthlyMeterSystemThreeMod.objects.all().order_by('date')
    entriesFuel = FuelLogSystemThreeMod.objects.all().order_by('date')
    return render(request,'systems/systemthree.html',{'entriesMonth':entriesMonth,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemFour(request):
    entriesMonth = monthlyMeterSystemFourMod.objects.all().order_by('date')
    entriesFuel = FuelLogSystemFourMod.objects.all().order_by('date')
    return render(request,'systems/systemfour.html',{'entriesMonth':entriesMonth,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemFive(request):
    entriesMonth = monthlyMeterSystemFiveMod.objects.all().order_by('date')
    entriesFuel = FuelLogSystemFiveMod.objects.all().order_by('date')
    return render(request,'systems/systemfive.html',{'entriesMonth':entriesMonth,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemSix(request):
    entriesMonth = monthlyMeterSystemSixMod.objects.all().order_by('date')
    entriesFuel = FuelLogSystemSixMod.objects.all().order_by('date')
    return render(request,'systems/systemsix.html',{'entriesMonth':entriesMonth,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemSeven(request):
    entriesMonth = monthlyMeterSystemSevenMod.objects.all().order_by('date')
    entriesFuel = FuelLogSystemSevenMod.objects.all().order_by('date')
    return render(request,'systems/systemseven.html',{'entriesMonth':entriesMonth,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemEight(request):
    entriesMonth = monthlyMeterSystemEightMod.objects.all().order_by('date')
    entriesFuel = FuelLogSystemEightMod.objects.all().order_by('date')
    return render(request,'systems/systemeight.html',{'entriesMonth':entriesMonth,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemNine(request):
    entriesMonth = monthlyMeterSystemNineMod.objects.all().order_by('date')
    entriesFuel = FuelLogSystemNineMod.objects.all().order_by('date')
    return render(request,'systems/systemnine.html',{'entriesMonth':entriesMonth,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemTen(request):
    entriesMonth = monthlyMeterSystemTenMod.objects.all().order_by('date')
    entriesFuel = FuelLogSystemTenMod.objects.all().order_by('date')
    return render(request,'systems/systemten.html',{'entriesMonth':entriesMonth,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def monthlySystemOne(request):
    entries = monthlyMeterSystemOneMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.MonthlyMeterOneForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            curr = instance.current_meter_reading
            pre = instance.previous_meter_reading
            now = curr - pre
            instance.difference = now
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        try:
            initial = {
            'previous_meter_reading': monthlyMeterSystemOneMod.objects.all().order_by('-id')[0].current_meter_reading
            }
        except:
            initial = {
            'previous_meter_reading': 0
            }
        form = forms.MonthlyMeterOneForm(initial=initial)
    return render(request,'systems/monthlysystemone.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def monthlySystemTwo(request):
    entries = monthlyMeterSystemTwoMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.MonthlyMeterTwoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            curr = instance.current_meter_reading
            pre = instance.previous_meter_reading
            now = curr - pre
            instance.difference = now
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        try:
            initial = {
            'previous_meter_reading': monthlyMeterSystemTwoMod.objects.all().order_by('-id')[0].current_meter_reading
            }
        except:
            initial = {
            'previous_meter_reading': 0
            }
        form = forms.MonthlyMeterTwoForm(initial=initial)
    return render(request,'systems/monthlysystemtwo.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def monthlySystemThree(request):
    entries = monthlyMeterSystemThreeMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.MonthlyMeterThreeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            curr = instance.current_meter_reading
            pre = instance.previous_meter_reading
            now = curr - pre
            instance.difference = now
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        try:
            initial = {
            'previous_meter_reading': monthlyMeterSystemThreeMod.objects.all().order_by('-id')[0].current_meter_reading
            }
        except:
            initial = {
            'previous_meter_reading': 0
            }
        form = forms.MonthlyMeterThreeForm(initial=initial)
    return render(request,'systems/monthlysystemthree.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def monthlySystemFour(request):
    entries = monthlyMeterSystemFourMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.MonthlyMeterFourForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            curr = instance.current_meter_reading
            pre = instance.previous_meter_reading
            now = curr - pre
            instance.difference = now
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        try:
            initial = {
            'previous_meter_reading': monthlyMeterSystemFourMod.objects.all().order_by('-id')[0].current_meter_reading
            }
        except:
            initial = {
            'previous_meter_reading': 0
            }
        form = forms.MonthlyMeterFourForm(initial=initial)
    return render(request,'systems/monthlysystemfour.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def monthlySystemFive(request):
    entries = monthlyMeterSystemFiveMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.MonthlyMeterFiveForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            curr = instance.current_meter_reading
            pre = instance.previous_meter_reading
            now = curr - pre
            instance.difference = now
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        try:
            initial = {
            'previous_meter_reading': monthlyMeterSystemFiveMod.objects.all().order_by('-id')[0].current_meter_reading
            }
        except:
            initial = {
            'previous_meter_reading': 0
            }
        form = forms.MonthlyMeterFiveForm(initial=initial)
    return render(request,'systems/monthlysystemfive.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def monthlySystemSix(request):
    entries = monthlyMeterSystemSixMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.MonthlyMeterSixForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            curr = instance.current_meter_reading
            pre = instance.previous_meter_reading
            now = curr - pre
            instance.difference = now
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        try:
            initial = {
            'previous_meter_reading': monthlyMeterSystemSixMod.objects.all().order_by('-id')[0].current_meter_reading
            }
        except:
            initial = {
            'previous_meter_reading': 0
            }
        form = forms.MonthlyMeterSixForm(initial=initial)
    return render(request,'systems/monthlysystemsix.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def monthlySystemSeven(request):
    entries = monthlyMeterSystemSevenMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.MonthlyMeterSevenForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            curr = instance.current_meter_reading
            pre = instance.previous_meter_reading
            now = curr - pre
            instance.difference = now
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        try:
            initial = {
            'previous_meter_reading': monthlyMeterSystemSevenMod.objects.all().order_by('-id')[0].current_meter_reading
            }
        except:
            initial = {
            'previous_meter_reading': 0
            }
        form = forms.MonthlyMeterSevenForm(initial=initial)
    return render(request,'systems/monthlysystemseven.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def monthlySystemEight(request):
    entries = monthlyMeterSystemEightMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.MonthlyMeterEightForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            curr = instance.current_meter_reading
            pre = instance.previous_meter_reading
            now = curr - pre
            instance.difference = now
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        try:
            initial = {
            'previous_meter_reading': monthlyMeterSystemEightMod.objects.all().order_by('-id')[0].current_meter_reading
            }
        except:
            initial = {
            'previous_meter_reading': 0
            }
        form = forms.MonthlyMeterEightForm(initial=initial)
    return render(request,'systems/monthlysystemeight.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def monthlySystemNine(request):
    entries = monthlyMeterSystemNineMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.MonthlyMeterNineForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            curr = instance.current_meter_reading
            pre = instance.previous_meter_reading
            now = curr - pre
            instance.difference = now
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        try:
            initial = {
            'previous_meter_reading': monthlyMeterSystemNineMod.objects.all().order_by('-id')[0].current_meter_reading
            }
        except:
            initial = {
            'previous_meter_reading': 0
            }
        form = forms.MonthlyMeterNineForm(initial=initial)
    return render(request,'systems/monthlysystemnine.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def monthlySystemTen(request):
    entries = monthlyMeterSystemTenMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.MonthlyMeterTenForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            curr = instance.current_meter_reading
            pre = instance.previous_meter_reading
            now = curr - pre
            instance.difference = now
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        try:
            initial = {
            'previous_meter_reading': monthlyMeterSystemTenMod.objects.all().order_by('-id')[0].current_meter_reading
            }
        except:
            initial = {
            'previous_meter_reading': 0
            }
        form = forms.MonthlyMeterTenForm(initial=initial)
    return render(request,'systems/monthlysystemten.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def fuelLogSystemOne(request):
    entries = FuelLogSystemOneMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.AddFuelLogOneForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.AddFuelLogOneForm()
    return render(request,'systems/fuellogsystemone.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def fuelLogSystemTwo(request):
    entries = FuelLogSystemTwoMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.AddFuelLogTwoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.AddFuelLogTwoForm()
    return render(request,'systems/fuellogsystemtwo.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def fuelLogSystemThree(request):
    entries = FuelLogSystemThreeMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.AddFuelLogThreeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.AddFuelLogThreeForm()
    return render(request,'systems/fuellogsystemthree.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def fuelLogSystemFour(request):
    entries = FuelLogSystemFourMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.AddFuelLogFourForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.AddFuelLogFourForm()
    return render(request,'systems/fuellogsystemfour.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def fuelLogSystemFive(request):
    entries = FuelLogSystemFiveMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.AddFuelLogFiveForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.AddFuelLogFiveForm()
    return render(request,'systems/fuellogsystemfive.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def fuelLogSystemSix(request):
    entries = FuelLogSystemSixMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.AddFuelLogSixForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.AddFuelLogSixForm()
    return render(request,'systems/fuellogsystemsix.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def fuelLogSystemSeven(request):
    entries = FuelLogSystemSevenMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.AddFuelLogSevenForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.AddFuelLogSevenForm()
    return render(request,'systems/fuellogsystemseven.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def fuelLogSystemEight(request):
    entries = FuelLogSystemEightMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.AddFuelLogEightForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.AddFuelLogEightForm()
    return render(request,'systems/fuellogsystemeight.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def fuelLogSystemNine(request):
    entries = FuelLogSystemNineMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.AddFuelLogNineForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.AddFuelLogNineForm()
    return render(request,'systems/fuellogsystemnine.html',{'form':form,'entry':entries})

@login_required(login_url="/accounts/login/")
def fuelLogSystemTen(request):
    entries = FuelLogSystemTenMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.AddFuelLogTenForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.AddFuelLogTenForm()
    return render(request,'systems/fuellogsystemten.html',{'form':form,'entry':entries})
