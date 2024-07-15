from django.db import models
from django.utils.translation import gettext_lazy as _

from handout.models import Handout
from users.models import User
from utils.base_model import BaseModel


class Like(BaseModel):
    client_ip = models.GenericIPAddressField(verbose_name=_("client_ip"), max_length=150)
    user = models.ForeignKey(
        User,
        related_name="likes",
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    handout = models.ForeignKey(
        Handout,
        verbose_name=_("handout"),
        on_delete=models.CASCADE,
        related_name="hlike",
    )

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
        constraints = [models.UniqueConstraint(fields=["user", "handout"], name="unique_user_handout_like")]

    def __str__(self):
        return f"{self.handout}_{self.user}"
