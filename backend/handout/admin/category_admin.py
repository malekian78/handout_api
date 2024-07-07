from django.contrib import admin
from handout.models import Category
from django.utils.translation import gettext_lazy as _


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent", "updated_at", "created_at")
    list_display_links = ("id", "name", "parent")
    list_filter = ("name", "parent", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("created_at",)
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (
            _("Category Fields"),
            {
                "fields": ("name", "parent", "slug"),
            },
        ),
    )
