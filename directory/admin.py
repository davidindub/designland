from django.contrib import admin
from .models import Resource, Comment

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("approved", "created_on")
    list_display = ("title", "author", "created_on", "approved")
    actions = ["approve_resource"]

    def approve_resource(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ("approved", "created_on")
    list_display = ("resource", "body", "author", "created_on", "approved")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
            queryset.update(approved=True)
