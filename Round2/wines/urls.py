from django.urls import path
from . import views

app_name='wines'

urlpatterns = [
    path('',views.wines_view,name="list"),
    path('filter/variety/',views.filter_wines,name="byVariety"),
    path('filter/country/',views.filter_wines,name="byCountry"),
    path('filter/province/',views.filter_wines,name="byProvince"),
    path('filter/region/',views.filter_wines,name="byRegion"),
    path('filter/sortByPrice/',views.wines_view,name="sortByPrice")
]
