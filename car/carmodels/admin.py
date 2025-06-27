from django.contrib import admin
from django .http import HttpResponse
from .models import Car

class Caradmin(admin.ModelAdmin):
    list_display=('carname','price','colour','image')
admin.site.register(Car,Caradmin)

# Register your models here.
   