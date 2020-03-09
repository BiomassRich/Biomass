from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('systems/' ,include('systems.urls')),
    path('fueldelivery/' ,include('fueldelivery.urls')),
    path('',views.homepage,name="home"),
]
urlpatterns += staticfiles_urlpatterns()
