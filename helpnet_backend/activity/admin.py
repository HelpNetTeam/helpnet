from django.contrib import admin
from .models.activity import (
    Activity,
    ActivityComment,
    ActivityNeed,
    ActivityRating,
    )
from .models.project import Project


admin.site.register(Activity)
admin.site.register(ActivityComment)
admin.site.register(ActivityNeed)
admin.site.register(ActivityRating)
admin.site.register(Project)
