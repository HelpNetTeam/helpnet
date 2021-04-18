from django.contrib import admin
from .models.activity import (
    Activity,
    Comment,
    CommentLike,
    NeedActivity,
    Review,
    )
from .models.project import Project
from .models.organization import Organization
from .models.category import Category
from .models.need import Need, NeedUom
from .models.profile import Profile


admin.site.register(Activity)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(NeedActivity)
admin.site.register(Review)
admin.site.register(Project)
admin.site.register(Organization)
admin.site.register(Category)
admin.site.register(Need)
admin.site.register(NeedUom)
admin.site.register(Profile)

