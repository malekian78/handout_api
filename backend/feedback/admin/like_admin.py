from django.contrib import admin

from feedback.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "client_ip", "handout", "updated_at", "created_at")
    list_display_links = (
        "id",
        "user",
        "client_ip",
    )
    list_filter = ("handout", "created_at", "updated_at")
    search_fields = ("handout",)
    ordering = ("created_at",)
