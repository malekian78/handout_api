from datetime import datetime
import os
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        order_with_respect_to = "created_at"

def validate_file_extension(value):
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf',]
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Unsupported file extension.'))

def get_upload_path(instance, filename):
    return 'documents/{0}/{1}'.format(instance.author.name, filename)
class Handout(BaseModel):
    name = models.CharField(verbose_name=_("Handout name"), max_length=100)
    slug = models.SlugField(verbose_name=_("access"), unique=True, auto_created=True, help_text=_("by this link users will access to this Handout."))
    description = models.TextField(verbose_name=_("description"),max_length=500)
    page_count = models.PositiveIntegerField(verbose_name=_("page count"))
    visit_count = models.PositiveIntegerField(verbose_name=_("View count"), default=0)
    publish_time = models.DateField(verbose_name=_("publish date"))
    author = models.ForeignKey("Author", verbose_name=_("author"), on_delete=models.DO_NOTHING, null=True, blank=True)
    file_size = models.PositiveIntegerField(verbose_name=_("file size"), editable=False)
    file_name = models.CharField(verbose_name=_("file name"), max_length=150, editable=False)
    file = models.FileField(verbose_name=_("file to upload"), upload_to=get_upload_path , validators=[validate_file_extension])
    category = models.ManyToManyField("Category", verbose_name=_("category"), blank=True)
    tag = models.ManyToManyField("Tag", verbose_name=_("tag"), blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = _("Handout")
        
    def save(self, *args, **kwargs):
        if self.file:
            self.file_name = self.file.name
            self.file_size = self.file.size
            self.file.name = self.get_custom_file_name(self.file.name)
        super().save(*args, **kwargs)
        
    def get_custom_file_name(self, original_filename):
        # Custom logic to rename the file
        name, ext = os.path.splitext(original_filename)
        new_name = f"{self.name}_{datetime.now().strftime('%Y%m%d%H%M%S')}{ext}"
        return new_name
    
    


class Category(BaseModel):
    name = models.CharField(verbose_name=_("category name"), max_length=150)
    slug = models.SlugField(verbose_name=_("access link"), unique=True, auto_created=True, help_text=_("by this link users will access to this category page."))
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children', on_delete=models.CASCADE
    )
    
    def save(self, *args, **kwargs):
        # prevent a category to be itself parent
        if self.id and self.parent and self.id == self.parent.id:
            self.parent = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = _("Category")


class Tag(BaseModel):
    name = models.CharField(verbose_name=_("tag name"), max_length=150)
    slug = models.SlugField(verbose_name=_("access link"), unique=True, auto_created=True, help_text=_("by this link users will access to this Tag page."))
    # handout = models.ManyToManyField(Handout, verbose_name=_("جزوه مربوطه", on_delete=models.DO_NOTHING, null=True, blank=True )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = _("Tag")

class Author(BaseModel):
    name = models.CharField(verbose_name=_("author name"), max_length=150)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = _("Author")

#? ManyToMany relationship
# class HandoutTags(BaseModel):
#     handout = models.ForeignKey(Handout, verbose_name=_("جزوه")
#     def __str__(self):
#         return self.handout
#     class Meta:
#         order_with_respect_to = "created_at"

# ? ManyToManty relationship
# class HandoutCategory(BaseModel):
#     pass

