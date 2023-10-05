from django.contrib import admin
from django.urls import include, path
from myapp.views import ProjectCreate, ProjectList, ProjectDetail, ProjectUpdate, ProjectDelete

urlpatterns = [
    path('create/', ProjectCreate.as_view(), name='create-project'),
    path('', ProjectList.as_view()),
    path('<uuid:_id>/', ProjectDetail.as_view(), name='retrieve-project'),
    path('update/<uuid:_id>/', ProjectUpdate.as_view(), name='update-project'),
    path('delete/<uuid:_id>/', ProjectDelete.as_view(), name='delete-project'),
]