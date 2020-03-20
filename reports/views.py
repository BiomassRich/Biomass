from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from systems.models import *

@login_required(login_url="/accounts/login/")
def systemOneFuelLogReport(request):
    entriesFuel = FuelLogSystemOneMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/','')
            todate = todate.replace('/','')
            return render(request,'reports/systemonefuellogreport.html',{'fromdate':fromdate,'todate':todate,'form':form,'entriesFuel':entriesFuel})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemonefuellogreport.html',{'form':form,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemTwoFuelLogReport(request):
    entriesFuel = FuelLogSystemTwoMod.objects.all().order_by('date')
    return render(request,'reports/systemtwofuellogreport.html',{'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemThreeFuelLogReport(request):
    entriesFuel = FuelLogSystemThreeMod.objects.all().order_by('date')
    return render(request,'reports/systemthreefuellogreport.html',{'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemFourFuelLogReport(request):
    entriesFuel = FuelLogSystemFourMod.objects.all().order_by('date')
    return render(request,'reports/systemfourfuellogreport.html',{'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemFiveFuelLogReport(request):
    entriesFuel = FuelLogSystemFiveMod.objects.all().order_by('date')
    return render(request,'reports/systemfivefuellogreport.html',{'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemSixFuelLogReport(request):
    entriesFuel = FuelLogSystemSixMod.objects.all().order_by('date')
    return render(request,'reports/systemsixfuellogreport.html',{'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemSevenFuelLogReport(request):
    entriesFuel = FuelLogSystemSevenMod.objects.all().order_by('date')
    return render(request,'reports/systemsevenfuellogreport.html',{'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemEightFuelLogReport(request):
    entriesFuel = FuelLogSystemEightMod.objects.all().order_by('date')
    return render(request,'reports/systemeightfuellogreport.html',{'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemNineFuelLogReport(request):
    entriesFuel = FuelLogSystemNineMod.objects.all().order_by('date')
    return render(request,'reports/systemninefuellogreport.html',{'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemTenFuelLogReport(request):
    entriesFuel = FuelLogSystemTenMod.objects.all().order_by('date')
    return render(request,'reports/systemtenfuellogreport.html',{'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemOneMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemOneMod.objects.all().order_by('date')
    return render(request,'reports/systemonemonthlyreport.html',{'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemTwoMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemTwoMod.objects.all().order_by('date')
    return render(request,'reports/systemtwomonthlyreport.html',{'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemThreeMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemThreeMod.objects.all().order_by('date')
    return render(request,'reports/systemthreemonthlyreport.html',{'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemFourMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemFourMod.objects.all().order_by('date')
    return render(request,'reports/systemfourmonthlyreport.html',{'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemFiveMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemFiveMod.objects.all().order_by('date')
    return render(request,'reports/systemfivemonthlyreport.html',{'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemSixMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemSixMod.objects.all().order_by('date')
    return render(request,'reports/systemsixmonthlyreport.html',{'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemSevenMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemSevenMod.objects.all().order_by('date')
    return render(request,'reports/systemsevenmonthlyreport.html',{'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemEightMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemEightMod.objects.all().order_by('date')
    return render(request,'reports/systemeightmonthlyreport.html',{'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemNineMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemNineMod.objects.all().order_by('date')
    return render(request,'reports/systemninemonthlyreport.html',{'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemTenMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemTenMod.objects.all().order_by('date')
    return render(request,'reports/systemtenmonthlyreport.html',{'entriesMonth':entriesMonth})
