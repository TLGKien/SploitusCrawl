import uuid
from django.db import models

# Create your models here.

class Project(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    projectName = models.CharField(null=False, blank=False, max_length=100)
    projectDescription = models.CharField(null=True, blank=False, max_length=250)
    partner = models.CharField(null=False, blank=False, max_length=40)
    manager = models.CharField(null=False, blank=False, max_length=40)
    startDate = models.DateField(null =False, blank=False, auto_now=False, auto_now_add=False)
    dueDate = models.DateField(null=True, blank=False, auto_now=False, auto_now_add=False)
    budget = models.FloatField(null=True, blank=False)
    status = models.CharField(null=False, blank=False, max_length=10)

    @classmethod
    def create(cls, projectName, projectDescription, partner, manager, startDate, dueDate, budget, status):
        test_record = cls(projectName = projectName, projectDescription = projectDescription, 
                          partner = partner, manager = manager, startDate = startDate, 
                          dueDate = dueDate, budget = budget, status = status)
        return test_record
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.projectName
    
    class Meta:
        app_label = 'myapp'