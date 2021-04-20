from django.urls import path
from .views.post_views import PostDetails, PostList
    
urlpatterns = [
    path('post', PostList.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetails.as_view(), name='post-detail'),
]
