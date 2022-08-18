from django.contrib import admin
from .models import Resource, Profile

admin.site.register(Profile)

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("approved", "created_on")
    list_display = ("title", "author", "created_on", "approved")
    actions = ["approve_resource"]

    def approve_resource(self, request, queryset):
        queryset.update(approved=True)