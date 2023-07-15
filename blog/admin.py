from django.contrib import admin
from .models import (
    Blog,
    Like,
    Category,
    Comment,
    PostViewRecords,
)


admin.site.register(Blog)
admin.site.register(Like)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostViewRecords)
