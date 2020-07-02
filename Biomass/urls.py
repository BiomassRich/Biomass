from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls import handler404, handler500


urlpatterns = [
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('systems/' ,include('systems.urls')),
    path('fueldelivery/' ,include('fueldelivery.urls')),
    path('products/' ,include('products.urls')),
    path('reports/' ,include('reports.urls')),
    path('permit/',views.permit,name="permit"),
    path('',views.homepage,name="home"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error_404
handler500 = views.error_500
