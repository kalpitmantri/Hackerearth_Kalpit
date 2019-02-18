from django.contrib import admin
from .models import Wines
from import_export.admin import ImportExportModelAdmin

@admin.register(Wines)
class WinesAdmin(ImportExportModelAdmin):
    pass
