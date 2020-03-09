from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = "accounts"

urlpatterns = [
    path('login/', views.login_view,name="login"),
    path('logout/',views.logout_view,name='logout'),
]
