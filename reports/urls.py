from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'reports'

urlpatterns = [
    path('onefuellogreport',views.systemOneFuelLogReport, name='onefuellogreport'),
    path('onemonthlyreport',views.systemOneMonthlyMeterReport, name='onemonthlyreport'),
    path('twofuellogreport',views.systemTwoFuelLogReport, name='twofuellogreport'),
    path('twomonthlyreport',views.systemTwoMonthlyMeterReport, name='twomonthlyreport'),
    path('threefuellogreport',views.systemThreeFuelLogReport, name='threefuellogreport'),
    path('threemonthlyreport',views.systemThreeMonthlyMeterReport, name='threemonthlyreport'),
    path('fourfuellogreport',views.systemFourFuelLogReport, name='fourfuellogreport'),
    path('fourmonthlyreport',views.systemFourMonthlyMeterReport, name='fourmonthlyreport'),
    path('fivefuellogreport',views.systemFiveFuelLogReport, name='fivefuellogreport'),
    path('fivemonthlyreport',views.systemFiveMonthlyMeterReport, name='fivemonthlyreport'),
    path('sixfuellogreport',views.systemSixFuelLogReport, name='sixfuellogreport'),
    path('sixmonthlyreport',views.systemSixMonthlyMeterReport, name='sixmonthlyreport'),
    path('sevenfuellogreport',views.systemSevenFuelLogReport, name='sevenfuellogreport'),
    path('sevenmonthlyreport',views.systemSevenMonthlyMeterReport, name='sevenmonthlyreport'),
    path('eightfuellogreport',views.systemEightFuelLogReport, name='eightfuellogreport'),
    path('eightmonthlyreport',views.systemEightMonthlyMeterReport, name='eightmonthlyreport'),
    path('ninefuellogreport',views.systemNineFuelLogReport, name='ninefuellogreport'),
    path('ninemonthlyreport',views.systemNineMonthlyMeterReport, name='ninemonthlyreport'),
    path('tenfuellogreport',views.systemTenFuelLogReport, name='tenfuellogreport'),
    path('tenmonthlyreport',views.systemTenMonthlyMeterReport, name='tenmonthlyreport'),
]
