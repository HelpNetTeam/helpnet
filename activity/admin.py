from django.contrib import admin
from .models.activity import (
    Activity,
    Comment,
    NeedActivity,
    Rating,
    )
from .models.project import Project
from .models.organization import Organization
from .models.category import Category
from .models.need import Need, NeedUom


admin.site.register(Activity)
admin.site.register(Comment)
admin.site.register(NeedActivity)
admin.site.register(Rating)
admin.site.register(Project)
admin.site.register(Organization)
admin.site.register(Category)
admin.site.register(Need)
admin.site.register(NeedUom)
