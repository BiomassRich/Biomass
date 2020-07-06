from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.urls import path

app_name = 'schedule'
urlpatterns = [
    path('index', views.index, name='index'),
    path('calendar', login_required(views.CalendarView.as_view()), name='calendar'),
    url(r'^event/new/$', login_required(views.event), name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', login_required(views.event), name='event_edit'),
]
