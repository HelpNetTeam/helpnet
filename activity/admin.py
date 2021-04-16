from django.contrib import admin
from .models.activity import (
    Activity,
    Comment,
    Need,
    Rating,
    )
from .models.project import Project
from .models.organization import Organization


admin.site.register(Activity)
admin.site.register(Comment)
admin.site.register(Need)
admin.site.register(Rating)
admin.site.register(Project)
admin.site.register(Organization)
