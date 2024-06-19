from django.contrib import admin
from .models import Comment, Like

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # setting filds of what to showing in admin-dashboard
    model = Comment
    list_display = ("id", "name", "email", "handout", "status_choice", "updated_at", "created_at")
    list_display_links = ("id", "name", "email", "handout",)
    list_filter = ("name", "created_at", "updated_at")
    list_editable = ( "status_choice",)
    search_fields = ("name", "email",)
    ordering = ("created_at",)
    

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    # setting filds of what to showing in admin-dashboard
    model = Like
    list_display = ("id", "user", "client_ip", "handout", "updated_at", "created_at")
    list_display_links = ("id", "user", "client_ip",)
    list_filter = ("handout", "created_at", "updated_at")
    search_fields = ("handout",)
    ordering = ("created_at",)
