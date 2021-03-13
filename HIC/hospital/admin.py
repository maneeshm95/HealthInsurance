from django.contrib import admin
from . models import Hospital, Hospital_type

# admin.site.register(Hospital)
# admin.site.register(Hospital_type)

class HospitalAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':('name',)
    }
admin.site.register(Hospital,HospitalAdmin)

admin.site.register(Hospital_type)