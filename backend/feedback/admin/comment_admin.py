from django.contrib import admin
from feedback.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "handout", "status", "updated_at", "created_at")
    list_display_links = ("id", "name", "email", "handout",)
    list_filter = ("name", "created_at", "updated_at")
    list_editable = ( "status",)
    search_fields = ("name", "email",)
    ordering = ("created_at",)