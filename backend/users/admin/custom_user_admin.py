from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ..models.custom_user import User
from django.utils.translation import gettext_lazy as _
# Register your models here.

class CustomUserAdmin(UserAdmin):
    # setting filds of what to showing in admin-dashboard
    model = User
    list_display = ("id", "email", "is_superuser", "is_active", "is_staff", "created_date")
    list_display_links = ("id", "email")
    list_filter = ("email", "is_superuser", "is_active", "is_staff", "created_date")
    list_editable = ( "is_active", "is_staff",)
    list_per_page = 20 # default == 100.
    readonly_fields = ("is_superuser",)
    search_fields = ("email",)
    ordering = ("created_date",)
    fieldsets = (
        (_('Authentication'), {
            'fields': (
                "email", "password"
            ),
        }),
        (_('Permissions'), {
            'fields': (
                "is_staff", "is_active","is_superuser"
            ),
        }),
    )
    # setting fields for adding and save new User by admin-dashboard
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active",
            )}
        ),
    )

admin.site.register(User, CustomUserAdmin)