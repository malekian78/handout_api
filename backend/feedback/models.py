from users.models import User
from handout.models import BaseModel, Handout
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# from ..handout.models import BaseModel, Handout



class Comment(BaseModel):
    handout = models.ForeignKey(Handout, verbose_name=_("handout"), on_delete=models.CASCADE, help_text=_("for wich handout this comment sended?"))
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
    client_ip = models.CharField(verbose_name=_("client_ip"), max_length=150, unique=True, blank=True, null=True)
    user = models.ForeignKey(User , verbose_name=_("user"), on_delete=models.CASCADE, blank=True, null=True)
    handout = models.ForeignKey(Handout, verbose_name=_("handout"), on_delete=models.CASCADE)
    def __str__(self):
        return "{}_{}".format(self.handout, self.user)
    class Meta:
        verbose_name_plural = _("Like")

    def save(self, *args, **kwargs):
        # prevent a category to be itself parent
        if self.client_ip is None and self.user is None:
            self.unique_error_message("test")
            return
            # raise ValueError(_("client_ip and user could not be null for both"))
        super().save(*args, **kwargs)
    
