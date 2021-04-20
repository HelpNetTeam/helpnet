from django.urls import path
from .views.profile_views import ProfileDetails, ProfileCreate
    
urlpatterns = [
    path('profile', ProfileCreate.as_view(), name='profile-create'),
    path('profile/<int:pk>', ProfileDetails.as_view(), name='profile-detail'),
]
