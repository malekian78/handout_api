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

class Handout(BaseModel):
    name = models.CharField(verbose_name=_("نام جزوه"), max_length=100)
    slug = models.SlugField(verbose_name=_("لینک دسترسی"), unique=True, auto_created=True, help_text="کاربران از طریق این لینک به صفحه جزوه دسترسی پیدا خواهند کرد")
    description = models.TextField(verbose_name=_("توضیحات"),max_length=500)
    file_name = models.CharField(verbose_name=_("نام فایل"), max_length=150, editable=False)
    page_count = models.PositiveIntegerField(verbose_name=_("تعداد صفحات جزوه"))
    file_size = models.PositiveIntegerField(verbose_name=_("اندازه فایل"), editable=False)
    visit_count = models.PositiveIntegerField(verbose_name=_("تعداد بازدید"), default=0)
    publish_time = models.DateField(verbose_name=_("تاریخ انتشار"))
    author = models.ForeignKey("Author", verbose_name=_("نویسنده"), on_delete=models.DO_NOTHING, null=True, blank=True)
    file = models.FileField(verbose_name=_("آپلود فایل"), upload_to='uploads/{}/{}'.format(author, file_name), validators=[validate_file_extension])
    category = models.ManyToManyField("Category", verbose_name=_("دسته بندی"), blank=True)
    tag = models.ManyToManyField("Tag", verbose_name=_("تگ"), blank=True)
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
    name = models.CharField(verbose_name=_("نام دسته بندی"), max_length=150)
    slug = models.SlugField(verbose_name=_("لینک دسترسی"), unique=True, auto_created=True, help_text="کاربران از طریق این لینک به صفحه دسته بندی مورد نظر دسترسی پیدا خواهند کرد")
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
    name = models.CharField(verbose_name=_("نام تگ"), max_length=150)
    slug = models.SlugField(verbose_name=_("لینک دسترسی"), unique=True, auto_created=True, help_text="کاربران از طریق این لینک به صفحه تگ مورد نظر دسترسی پیدا خواهند کرد")
    # handout = models.ManyToManyField(Handout, verbose_name=_("جزوه مربوطه", on_delete=models.DO_NOTHING, null=True, blank=True )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = _("Tag")

class Author(BaseModel):
    name = models.CharField(verbose_name=_("نام نویسنده"), max_length=150)
    
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

