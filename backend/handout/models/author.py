from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.base_model import BaseModel


class Author(BaseModel):
    name = models.CharField(verbose_name=_("author name"), max_length=150)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.name
