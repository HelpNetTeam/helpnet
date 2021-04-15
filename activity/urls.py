from django.urls import path
from .views.activitiy_views import ActivityList, ActivityDetails
from .views.project_views import ProjectList, ProjectDetails

urlpatterns = [
    path('activity', ActivityList.as_view(), name='activity_list'),
    path('activity/<int:id>', ActivityDetails.as_view(), name='activity_detail'),
    path('project', ProjectList.as_view(), name='project_list'),
    path('project/<int:id>', ProjectDetails.as_view(), name='project_detail'),
]
