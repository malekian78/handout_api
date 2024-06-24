from django.contrib import admin
from handout.models import Handout
from django.utils.translation import gettext_lazy as _

@admin.register(Handout)
class HandoutAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "publish_time", "author", "visit_count", "updated_at", "created_at")
    prepopulated_fields = {'slug':('name',)}
    list_display_links = ("id", "name", "author",)
    list_filter = ("name", "created_at", "updated_at")
    list_editable = ("publish_time", )
    readonly_fields = ("visit_count",)
    search_fields = ("name", "publish_time", "author",)
    ordering = ("created_at", "publish_time",)