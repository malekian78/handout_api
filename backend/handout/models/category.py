from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.base_model import BaseModel

class Category(BaseModel):
    name = models.CharField(verbose_name=_("category name"), max_length=150)
    slug = models.SlugField(verbose_name=_("access link"), unique=True, help_text=_("by this link users will access to this category page."))
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children', on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")
        
    def save(self, *args, **kwargs):
        # prevent a category to be itself parent
        if self.id and self.parent and self.id == self.parent.id:
            self.parent = None
        super().save(*args, **kwargs)

    def __str__(self):
            return self.name