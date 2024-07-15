from django.contrib import admin

from handout.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "updated_at", "created_at")
    list_display_links = ("id", "name")
    list_filter = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("created_at",)
