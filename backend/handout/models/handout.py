from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.base_model import BaseModel
from django.core.validators import FileExtensionValidator 

def get_upload_path(instance, filename):
    return f'handouts/{instance.author.name}/{filename}'

class Handout(BaseModel):
    name = models.CharField(verbose_name=_("Handout name"), max_length=100)
    slug = models.SlugField(verbose_name=_("access"), unique=True, help_text=_("by this link users will access to this Handout."))
    description = models.TextField(verbose_name=_("description"),max_length=500)
    page_count = models.PositiveIntegerField(verbose_name=_("page count"))
    visit_count = models.PositiveIntegerField(verbose_name=_("View count"), default=0)
    publish_time = models.DateField(verbose_name=_("publish date"))
    author = models.ForeignKey("Author", verbose_name=_("author"), on_delete=models.CASCADE, related_name="handout")
    file_size = models.PositiveIntegerField(verbose_name=_("file size"), editable=False)
    file_name = models.CharField(verbose_name=_("file name"), max_length=150)
    file = models.FileField(verbose_name=_("file to upload"), upload_to=get_upload_path, validators=[FileExtensionValidator(['pdf'])])
    category = models.ManyToManyField("Category", verbose_name=_("category"))
    tag = models.ManyToManyField("Tag", verbose_name=_("tag"), blank=True)
    class Meta:
        verbose_name = _("Handout")
        verbose_name_plural = _("Handouts")
    
    def __str__(self):
        return self.name    
    
    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size
        super().save(*args, **kwargs)    
    