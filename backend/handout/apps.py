from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HandoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'handout'
    verbose_name = _("handout Config")
    verbose_name_plural = _("handout Configs")