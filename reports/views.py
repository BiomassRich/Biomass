from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from systems.models import *
from datetime import datetime


@login_required(login_url="/accounts/login/")
def systemOneFuelLogReport(request):
    entriesFuel = FuelLogSystemOneMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesFuel = FuelLogSystemOneMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemonefuellogreport.html',{'form':form,'entriesFuel':entriesFuel})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemonefuellogreport.html',{'form':form,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemTwoFuelLogReport(request):
    entriesFuel = FuelLogSystemTwoMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesFuel = FuelLogSystemTwoMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemtwofuellogreport.html',{'form':form,'entriesFuel':entriesFuel})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemtwofuellogreport.html',{'form':form,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemThreeFuelLogReport(request):
    entriesFuel = FuelLogSystemThreeMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesFuel = FuelLogSystemThreeMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemthreefuellogreport.html',{'form':form,'entriesFuel':entriesFuel})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemthreefuellogreport.html',{'form':form,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemFourFuelLogReport(request):
    entriesFuel = FuelLogSystemFourMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesFuel = FuelLogSystemFourMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemfourfuellogreport.html',{'form':form,'entriesFuel':entriesFuel})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemfourfuellogreport.html',{'form':form,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemFiveFuelLogReport(request):
    entriesFuel = FuelLogSystemFiveMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesFuel = FuelLogSystemFiveMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemfivefuellogreport.html',{'form':form,'entriesFuel':entriesFuel})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemfivefuellogreport.html',{'form':form,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemSixFuelLogReport(request):
    entriesFuel = FuelLogSystemSixMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesFuel = FuelLogSystemSixMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemsixfuellogreport.html',{'form':form,'entriesFuel':entriesFuel})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemsixfuellogreport.html',{'form':form,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemSevenFuelLogReport(request):
    entriesFuel = FuelLogSystemSevenMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesFuel = FuelLogSystemSevenMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemsevenfuellogreport.html',{'form':form,'entriesFuel':entriesFuel})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemsevenfuellogreport.html',{'form':form,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemEightFuelLogReport(request):
    entriesFuel = FuelLogSystemEightMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesFuel = FuelLogSystemEightMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemeightfuellogreport.html',{'form':form,'entriesFuel':entriesFuel})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemeightfuellogreport.html',{'form':form,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemNineFuelLogReport(request):
    entriesFuel = FuelLogSystemNineMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesFuel = FuelLogSystemNineMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemninefuellogreport.html',{'form':form,'entriesFuel':entriesFuel})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemninefuellogreport.html',{'form':form,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemTenFuelLogReport(request):
    entriesFuel = FuelLogSystemTenMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesFuel = FuelLogSystemTenMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemtenfuellogreport.html',{'form':form,'entriesFuel':entriesFuel})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemtenfuellogreport.html',{'form':form,'entriesFuel':entriesFuel})

@login_required(login_url="/accounts/login/")
def systemOneMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemOneMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesMonth = monthlyMeterSystemOneMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemonemonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemonemonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemTwoMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemTwoMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesMonth = monthlyMeterSystemTwoMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemtwomonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemtwomonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemThreeMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemThreeMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesMonth = monthlyMeterSystemThreeMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemthreemonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemthreemonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemFourMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemFourMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesMonth = monthlyMeterSystemFourMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemfourmonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemfourmonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemFiveMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemFiveMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesMonth = monthlyMeterSystemFiveMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemfivemonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemfivemonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemSixMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemSixMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesMonth = monthlyMeterSystemSixMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemsixmonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemsixmonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemSevenMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemSevenMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesMonth = monthlyMeterSystemSevenMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemsevenmonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemsevenmonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemEightMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemEightMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesMonth = monthlyMeterSystemEightMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemeightmonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemeightmonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemNineMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemNineMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesMonth = monthlyMeterSystemNineMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemninemonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemninemonthlyreport.html',{'entriesMonth':entriesMonth})

@login_required(login_url="/accounts/login/")
def systemTenMonthlyMeterReport(request):
    entriesMonth = monthlyMeterSystemTenMod.objects.all().order_by('date')
    if request.method == 'POST':
        form = forms.ReportDateForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            fromdate = data.get('fromdate')
            todate = data.get('todate')
            fromdate = fromdate.replace('/',' ')
            todate = todate.replace('/',' ')
            fromdate = datetime.strptime(fromdate,'%d %m %Y')
            todate = datetime.strptime(todate,'%d %m %Y')
            entriesMonth = monthlyMeterSystemTenMod.objects.filter(day__gte=fromdate,day__lte=todate).order_by('date')
            return render(request,'reports/systemtenmonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})
    else:
        form = forms.ReportDateForm()
    return render(request,'reports/systemtenmonthlyreport.html',{'form':form,'entriesMonth':entriesMonth})
