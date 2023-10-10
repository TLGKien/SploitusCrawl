from django.shortcuts import render
from myapp.models import Project
from rest_framework import generics
from myapp.serializers import ProjectSerialiser


class ProjectCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerialiser

class ProjectList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Project.objects.all().order_by('startDate')
    serializer_class = ProjectSerialiser

class ProjectDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Project by pk.
    queryset = Project.objects.all()
    serializer_class = ProjectSerialiser
    lookup_field = '_id'

class ProjectUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Project record to be updated.
    queryset = Project.objects.all()
    serializer_class = ProjectSerialiser
    lookup_field = '_id'

class ProjectDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Project record to be deleted.
    queryset = Project.objects.all()
    serializer_class = ProjectSerialiser
    lookup_field = '_id'