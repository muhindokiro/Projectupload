from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =()
    
admin.site.register(Project)



# Register models here.
