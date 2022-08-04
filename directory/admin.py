from django.contrib import admin
from .models import Resource, Comment


# Auto creates the slug based on the title
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("approved", "created_on")
    list_display = ("title", "author", "created_on", "approved")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ("approved", "created_on")
    list_display = ("resource", "body", "author", "created_on", "approved")
