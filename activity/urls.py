from django.urls import path
from .views.activitiy_views import ActivityList, ActivityDetails, CommentDetails, CommentCreate, CommentActivityList #ReviewDetails, ReviewList
from .views.project_views import ProjectList, ProjectDetails
from .views.organization_views import OrganizationList, OrganizationDetails
from .views.category_views import CategoryList, CategoryDetails
from .views.need_views import NeedList, NeedDetails, NeedUomList, NeedUomDetails
from .views.profile_views import ProfileDetails

urlpatterns = [
    path('activity', ActivityList.as_view(), name='activity-list'),
    path('activity/<int:pk>', ActivityDetails.as_view(), name='activity-detail'),
    path('activity/<int:activity>/comment', CommentActivityList.as_view(), name='comment-list'),
    path('comment/<int:pk>', CommentDetails.as_view(), name='comment-detail'),
    path('comment', CommentCreate.as_view(), name='comment-create'),
    # path('activity/<int:pk>/review', ReviewList.as_view(), name='comment-list'),
    # path('activity/<int:pk>/review/<int:pk>', ReviewDetails.as_view(), name='comment-detail'),
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
    path('profile/<int:pk>', ProfileDetails.as_view(), name='profile-detail'),
]
