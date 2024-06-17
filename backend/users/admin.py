from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
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
        ('Authentication', {
            'fields': (
                "email", "password"
            ),
        }),
        ('Permissions', {
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
    #TODO: هم اضافه کن form یه فیلد
    # لینکش https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.form
    #TODO: Update the documentation if necessary.
#   TODO:  Note: the structure of the apps should be as follows:

# ├── users
# │   ├── admin
# │   │   ├── __init__.py
# │   │   ├── user.py
# │   ├── models
# │   │   ├── __init__.py
# │   │   ├── user.py
# │   ├── __init__.py
# │   ├── apps.py
# │   ├── urls.py

admin.site.register(User, CustomUserAdmin)

