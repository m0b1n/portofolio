from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    createDate = models.DateTimeField(null=False, default=now)
    deleteDate = models.DateTimeField(null=True, blank=True)
    isDeleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = now()
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return "{}, {}, {}".format(self.createDate, self.deleteDate, self.isDeleted)
