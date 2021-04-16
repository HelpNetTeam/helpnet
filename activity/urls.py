from django.urls import path
from .views.activitiy_views import ActivityList, ActivityDetails
from .views.project_views import ProjectList, ProjectDetails
from .views.organization_views import OrganizationList, OrganizationDetails

urlpatterns = [
    path('activity', ActivityList.as_view(), name='activity_list'),
    path('activity/<int:id>', ActivityDetails.as_view(), name='activity_detail'),
    path('project', ProjectList.as_view(), name='project_list'),
    path('project/<int:id>', ProjectDetails.as_view(), name='project_detail'),
    path('organization', OrganizationList.as_view(), name='organization_list'),
    path('organization/<int:id>', OrganizationDetails.as_view(), name='organization_detail'),
]
