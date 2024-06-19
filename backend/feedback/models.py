from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

#! i will replace this BaseModel class ...and use...  from handout.models import BaseModel
class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        order_with_respect_to = "created_at"

class Comment(BaseModel):
    # TODO: رو امپورت کنی Handout خود مدل "Handout" حتما باید به جای
    handout = models.ForeignKey("Handout", verbose_name=_("handout"), on_delete=models.CASCADE, help_text=_("for wich handout this comment sended?"))
    name = models.CharField(verbose_name=_("name"), max_length=150)
    email = models.EmailField(verbose_name=_("email"), max_length=150)
    body = models.TextField(verbose_name=_("Message"))
    status_choice = (
        ('draft', _('draft')),
        ('published', _('published')),
    )
    status = models.CharField(statusChoice=status_choice, verbose_name=_("status"), default="draft")

    def __str__(self):
        return "{}_{}".format(self.name, self.handout)
    class Meta:
        verbose_name_plural = _("Comment")


class Like(BaseModel):
    #! FIXME: یادت نره مدل یوزر رو بهش امپورت کنی
    # client_ip = ?
    user = models.ForeignKey("user" , verbose_name=_("user"), on_delete=models.CASCADE)
    handout = models.ForeignKey("handout", verbose_name=_("handout"), on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(verbose_name=_("rate"), max_length=1, default=1)
    def __str__(self):
        return "{}_{}".format(self.user, self.rate)
    class Meta:
        verbose_name_plural = _("Comment")
    



class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        order_with_respect_to = "created_at"

class Handout(BaseModel):
    name = models.CharField(verbose_name=_("نام جزوه"), max_length=100)
    slug = models.SlugField(verbose_name=_("لینک دسترسی"), unique=True, auto_created=True, help_text="کاربران از طریق این لینک به صفحه جزوه دسترسی پیدا خواهند کرد")
    description = models.TextField(verbose_name=_("توضیحات"),max_length=500)
    file_name = models.CharField(verbose_name=_("نام فایل"), max_length=150)
    page_count = models.PositiveIntegerField(verbose_name=_("تعداد صفحات جزوه"))
    file_size = models.PositiveIntegerField(verbose_name=_("اندازه فایل"))
    visit_count = models.PositiveIntegerField(verbose_name=_("تعداد بازدید"), default=0)
    publish_time = models.DateField(verbose_name=_("تاریخ انتشار"))
    author = models.ForeignKey("Author", verbose_name=_("نویسنده"), on_delete=models.DO_NOTHING, null=True, blank=True)
    file = models.FileField(verbose_name=_("آپلود فایل"), upload_to='uploads/{}/{}'.format(author, file_name))
    category = models.ManyToManyField("Category", verbose_name=_("دسته بندی"), blank=True)
    tag = models.ManyToManyField("Tag", verbose_name=_("تگ"), blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = _("Handout")

