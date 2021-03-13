from django.contrib import admin
from . models import Patient


#admin.site.register(Patient)

class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','age','gender']

admin.site.register(Patient, PatientAdmin)