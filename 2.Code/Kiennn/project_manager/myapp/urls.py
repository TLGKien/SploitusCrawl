from django.contrib import admin
from django.urls import include, path
from myapp.views import ProjectCreate, ProjectList, ProjectDetail, ProjectUpdate, ProjectDelete

urlpatterns = [
    path('create/', ProjectCreate.as_view(), name='create-customer'),
    path('', ProjectList.as_view()),
    path('<int:pk>/', ProjectDetail.as_view(), name='retrieve-customer'),
    path('update/<int:pk>/', ProjectUpdate.as_view(), name='update-customer'),
    path('delete/<int:pk>/', ProjectDelete.as_view(), name='delete-customer')
]