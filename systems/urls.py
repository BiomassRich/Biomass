from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'systems'

urlpatterns = [
    path('systemone',views.systemOne, name='systemone'),
    path('systemone/fuellog',views.fuelLogSystemOne, name="fuellogsystemone"),
    path('systemone/monthlymeter',views.monthlySystemOne,name='monthlysystemone'),
    path('systemtwo',views.systemTwo, name='systemtwo'),
    path('systemtwo/fuellog',views.fuelLogSystemTwo, name="fuellogsystemtwo"),
    path('systemtwo/monthlymeter',views.monthlySystemTwo,name='monthlysystemtwo'),
    path('systemthree',views.systemThree, name='systemthree'),
    path('systemthree/fuellog',views.fuelLogSystemThree, name="fuellogsystemthree"),
    path('systemthree/monthlymeter',views.monthlySystemThree,name='monthlysystemthree'),
    path('systemfour',views.systemFour, name='systemfour'),
    path('systemfour/fuellog',views.fuelLogSystemFour, name="fuellogsystemfour"),
    path('systemfour/monthlymeter',views.monthlySystemFour,name='monthlysystemfour'),
    path('systemfive',views.systemFive, name='systemfive'),
    path('systemfive/fuellog',views.fuelLogSystemFive, name="fuellogsystemfive"),
    path('systemfive/monthlymeter',views.monthlySystemFive,name='monthlysystemfive'),
    path('systemsix',views.systemSix, name='systemsix'),
    path('systemsix/fuellog',views.fuelLogSystemSix, name="fuellogsystemsix"),
    path('systemsix/monthlymeter',views.monthlySystemSix,name='monthlysystemsix'),
    path('systemseven',views.systemSeven, name='systemseven'),
    path('systemseven/fuellog',views.fuelLogSystemSeven, name="fuellogsystemseven"),
    path('systemseven/monthlymeter',views.monthlySystemSeven,name='monthlysystemseven'),
    path('systemeight',views.systemEight, name='systemeight'),
    path('systemeight/fuellog',views.fuelLogSystemEight, name="fuellogsystemeight"),
    path('systemeight/monthlymeter',views.monthlySystemEight,name='monthlysystemeight'),
    path('systemnine',views.systemNine, name='systemnine'),
    path('systemnine/fuellog',views.fuelLogSystemNine, name="fuellogsystemnine"),
    path('systemnine/monthlymeter',views.monthlySystemNine,name='monthlysystemnine'),
    path('systemten',views.systemTen, name='systemten'),
    path('systemten/fuellog',views.fuelLogSystemTen, name="fuellogsystemten"),
    path('systemten/monthlymeter',views.monthlySystemTen,name='monthlysystemten'),
    path('systemone/fuellog/<id>/',views.idfuelLogSystemOne, name='idfuellogsystemone'),
    path('systemone/monthlymeter/<id>/',views.idmonthlySystemOne, name='idmonthlysystemone'),
]
