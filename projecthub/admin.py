from django.contrib import admin
from .models import Project,Review,Profile

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =()
    
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Profile)

# Register models here.
