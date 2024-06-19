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
    status = models.CharField(choices= status_choice, verbose_name=_("status"), default="draft")

    def __str__(self):
        return "{}_{}".format(self.name, self.handout)
    class Meta:
        verbose_name_plural = _("Comment")


class Like(BaseModel):
    #! FIXME: یادت نره مدل یوزر رو بهش امپورت کنی
    client_ip = models.CharField(verbose_name=_("client_ip"), max_length=150, unique=True, blank=True, null=True)
    user = models.ForeignKey("User" , verbose_name=_("user"), on_delete=models.CASCADE, blank=True, null=True)
    handout = models.ForeignKey("Handout", verbose_name=_("handout"), on_delete=models.CASCADE)
    def __str__(self):
        return "{}_{}".format(self.user, self.rate)
    class Meta:
        verbose_name_plural = _("Comment")
    
    # FIXME: اگر نه کاربر و نه همچنین کلاینتی وجود داشت باید حتما اون فیلد ذخیره نشه
    
