from rest_framework import serializers
from myapp.models import Project

class ProjectSerialiser(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = Project
      fields = ("pk", "projectName", "projectDescription", 
                    "partner", "manager", "startDate", 
                    "dueDate", "budget", "status")
