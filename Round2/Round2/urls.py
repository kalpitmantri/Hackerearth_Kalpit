from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from wines import views as wine_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('wines/',include('wines.urls')),
    path('',wine_views.wines_view,name="home"),
]

urlpatterns += staticfiles_urlpatterns()