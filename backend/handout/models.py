from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Handout(BaseModel):
    name = models.CharField(verbose_name="نام جزوه", max_length=100)
    slug = models.SlugField(verbose_name="لینک دسترسی", unique=True, auto_created=True, help_text="کاربران از طریق این لینک به صفحه جزوه دسترسی پیدا خواهند کرد")
    description = models.TextField(verbose_name="توضیحات",max_length=500)
    # file = 
    file_name = models.CharField(verbose_name="نام فایل", max_length=150)
    page_count = models.PositiveIntegerField(verbose_name="تعداد صفحات جزوه")
    file_size = models.PositiveIntegerField(verbose_name="اندازه فایل")
    visit_count = models.PositiveIntegerField(verbose_name="تعداد بازدید", default=0)
    publish_time = models.DateField(verbose_name="تاریخ انتشار")
    author = models.ForeignKey("Author", verbose_name="نویسنده", on_delete=models.DO_NOTHING, null=True, blank=True)
    category = models.ManyToManyField("Category", verbose_name="دسته بندی", on_delete=models.DO_NOTHING, null=True, blank=True)
    tag = models.ManyToManyField("Tag", verbose_name="تگ", on_delete=models.DO_NOTHING, null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        order_with_respect_to = "created_at"


class Category(BaseModel):
    name = models.CharField(verbose_name="نام دسته بندی", max_length=150)
    slug = models.SlugField(verbose_name="لینک دسترسی", unique=True, auto_created=True, help_text="کاربران از طریق این لینک به صفحه دسته بندی مورد نظر دسترسی پیدا خواهند کرد")
    # parent = models.
    def __str__(self):
        return self.name
    class Meta:
        order_with_respect_to = "created_at"


class Tag(BaseModel):
    name = models.CharField(verbose_name="نام تگ", max_length=150)
    slug = models.SlugField(verbose_name="لینک دسترسی", unique=True, auto_created=True, help_text="کاربران از طریق این لینک به صفحه تگ مورد نظر دسترسی پیدا خواهند کرد")
    # handout = models.ManyToManyField(Handout, verbose_name="جزوه مربوطه", on_delete=models.DO_NOTHING, null=True, blank=True )
    def __str__(self):
        return self.name
    class Meta:
        order_with_respect_to = "created_at"

class Author(BaseModel):
    name = models.CharField(verbose_name="نام نویسنده", max_length=150)

#? it look like ManyToMany relationship
# class HandoutTags(BaseModel):
#     handout = models.ForeignKey(Handout, verbose_name="جزوه")
#     def __str__(self):
#         return self.handout
#     class Meta:
#         order_with_respect_to = "created_at"

# ? ManyToManty relationship
# class HandoutCategory(BaseModel):
#     pass

