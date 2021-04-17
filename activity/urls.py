from django.urls import path
from .views.activitiy_views import ActivityList, ActivityDetails, CommentDetails, CommentList
from .views.project_views import ProjectList, ProjectDetails
from .views.organization_views import OrganizationList, OrganizationDetails
from .views.category_views import CategoryList, CategoryDetails
from .views.need_views import NeedList, NeedDetails, NeedUomList, NeedUomDetails

urlpatterns = [
    path('activity', ActivityList.as_view(), name='activity_list'),
    path('activity/<int:pk>', ActivityDetails.as_view(), name='activity-detail'),
    path('comment', CommentList.as_view(), name='comment_list'),
    path('comment/<int:pk>', CommentDetails.as_view(), name='comment-detail'),
    path('project', ProjectList.as_view(), name='project_list'),
    path('project/<int:id>', ProjectDetails.as_view(), name='project_detail'),
    path('organization', OrganizationList.as_view(), name='organization_list'),
    path('organization/<int:id>', OrganizationDetails.as_view(), name='organization_detail'),
    path('category', CategoryList.as_view(), name='category_list'),
    path('category/<int:id>', CategoryDetails.as_view(), name='category_detail'),
    path('need', NeedList.as_view(), name='need_list'),
    path('need/<int:id>', NeedDetails.as_view(), name='need_detail'),
    path('need_uom', NeedUomList.as_view(), name='need_uom_list'),
    path('need_uom/<int:id>', NeedUomDetails.as_view(), name='need_uom_detail'),
]
