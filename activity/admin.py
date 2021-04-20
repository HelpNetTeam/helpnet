from django.contrib import admin
from core.models.profile import Profile
from .models.activity import (
    Activity,
    Comment,
    CommentLike,
    ActivityLike,
    NeedActivity,
    Review,
    )
from .models.project import Project
from .models.organization import Organization
from .models.category import Category
from .models.need import Need, NeedUom


admin.site.register(Activity)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(ActivityLike)
admin.site.register(NeedActivity)
admin.site.register(Review)
admin.site.register(Project)
admin.site.register(Organization)
admin.site.register(Category)
admin.site.register(Need)
admin.site.register(NeedUom)

