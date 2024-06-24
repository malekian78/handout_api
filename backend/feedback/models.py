from users.models import User
from handout.models import Handout
from utils.base_model import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Comment(BaseModel):
    handout = models.ForeignKey(Handout, verbose_name=_("handout"), on_delete=models.CASCADE, help_text=_("for wich handout this comment sended?"))
    name = models.CharField(verbose_name=_("name"), max_length=150)
    email = models.EmailField(verbose_name=_("email"), max_length=150)
    body = models.TextField(verbose_name=_("Message"))
    draft = 0
    published = 1
    rejected = 2
    status_choice = (
        (0, _('draft')),
        (1, _('published')),
        (2, _('rejected')),
    )
    status = models.PositiveSmallIntegerField(choices= status_choice, verbose_name=_("status"), default=0)
    class Meta:
            verbose_name = _("Comment")
            verbose_name_plural = _("Comments")
            
    def __str__(self):
        return f"{self.name}_{self.handout}"
    


class Like(BaseModel):
    client_ip = models.GenericIPAddressField(verbose_name=_("client_ip"), max_length=150)
    user = models.ForeignKey(User , verbose_name=_("user"), on_delete=models.CASCADE, blank=True, null=True)
    handout = models.ForeignKey(Handout, verbose_name=_("handout"), on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
    
    def __str__(self):
        return f"{self.handout}_{self.user}"
    
