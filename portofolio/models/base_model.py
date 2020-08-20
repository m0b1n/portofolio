from django.db import models
from django.utils.timezone import now
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_date = models.DateTimeField(null=False, default=now)
    delete_date = models.DateTimeField(null=True, blank=True)
    modification_date = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(null=False, default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = now()
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return "{}, {}, {}".format(self.create_date, self.delete_date, self.is_deleted)
