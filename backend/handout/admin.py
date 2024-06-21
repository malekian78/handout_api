from django.contrib import admin
from .models import Author, Category, Handout, Tag
from django.utils.translation import gettext_lazy as _
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # setting filds of what to showing in admin-dashboard
    model = Author
    list_display = ("id", "name", "updated_at", "created_at")
    list_display_links = ("id", "name")
    list_filter = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("created_at",)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # setting filds of what to showing in admin-dashboard
    model = Category
    list_display = ("id", "name", "parent", "updated_at", "created_at")
    list_display_links = ("id", "name", "parent")
    list_filter = ("name", "parent", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("created_at",)
    prepopulated_fields = {'slug':('name',)}
    fieldsets = (
        (_('Category Fields'), {
            'fields': (
                "name", "parent", "slug"
            ),
        }),
    )

@admin.register(Handout)
class HandoutAdmin(admin.ModelAdmin):
    # setting filds of what to showing in admin-dashboard
    model = Handout
    list_display = ("id", "name", "publish_time", "author", "visit_count", "updated_at", "created_at")
    prepopulated_fields = {'slug':('name',)}
    list_display_links = ("id", "name", "author",)
    list_filter = ("name", "created_at", "updated_at")
    list_editable = ("publish_time", )
    readonly_fields = ("visit_count",)
    search_fields = ("name", "publish_time", "author",)
    ordering = ("created_at", "publish_time",)

@admin.register(Tag)
class TagrAdmin(admin.ModelAdmin):
    # setting filds of what to showing in admin-dashboard
    model = Tag
    list_display = ("id", "name", "updated_at", "created_at")
    list_display_links = ("id", "name")
    list_filter = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("created_at",)
    prepopulated_fields = {'slug':('name',)}

