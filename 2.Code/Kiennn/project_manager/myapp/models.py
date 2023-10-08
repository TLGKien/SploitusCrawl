import uuid
from django.db import models

# Create your models here.

class Project(models.Model):
    CHOICES = (
        ('Chờ xét duyệt', 'Chờ xét duyệt'),
        ('Được chấp thuận', 'Được chấp thuận'),
        ('Bị từ chối', 'Bị từ chối'),
        ('Đã hoàn thành', 'Đã hoàn thành'),
    )

    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    projectName = models.CharField(null=False, blank=False, unique=True, max_length=100)
    projectDescription = models.CharField(null=True, blank=True,max_length=250)
    partner = models.CharField(null=True, blank=True,max_length=40)
    manager = models.CharField(null=True, blank=True,max_length=40)
    startDate = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    dueDate = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    budget = models.FloatField(null=True, blank=True,default=0.0)
    status = models.CharField(null=False, blank=False, choices=CHOICES, default="Chờ xét duyệt")

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