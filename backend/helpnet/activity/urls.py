from django.urls import path
from .views import activity_list, activity_detail

urlpatterns = [
    path('activity', activity_list),
    path('activity/<int:id>', activity_detail)
]