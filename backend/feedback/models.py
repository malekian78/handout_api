from django.db import models
from django.utils import timezone

#! i will replace this BaseModel class ...and use...  from handout.models import BaseModel
class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

