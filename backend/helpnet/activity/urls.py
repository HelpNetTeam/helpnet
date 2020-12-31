from django.urls import path
from .views import ActivityList, ActivityDetails

urlpatterns = [
    path('activity', ActivityList.as_view()),
    path('activity/<int:id>', ActivityDetails.as_view()),
]
