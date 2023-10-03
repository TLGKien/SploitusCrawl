from django.contrib import admin
from myapp.models import Project

# Register your models here.

@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ["_id", "projectName", "projectDescription", 
                    "partner", "manager", "startDate", 
                    "dueDate", "budget", "status"]
    admin.register(Project)