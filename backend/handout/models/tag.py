from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.base_model import BaseModel

class Tag(BaseModel):
    name = models.CharField(verbose_name=_("tag name"), max_length=150)
    slug = models.SlugField(verbose_name=_("access link"), unique=True, help_text=_("by this link users will access to this Tag page."))
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
    
    def __str__(self):
        return self.name