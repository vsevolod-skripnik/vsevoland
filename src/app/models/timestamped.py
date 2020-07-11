from django.db import models
from django.utils import timezone

from app.models.default import DefaultModel


class Timestamped(models.Model):
    """
    An abstract behavior representing timestamped model
    with `created_at` and `updated_at` fields.
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    updated_at = models.DateTimeField(
        null=True,
        blank=True,
        db_index=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.id:
            self.updated_at = timezone.now()
        return super(Timestamped, self).save(*args, **kwargs)


class TimestampedModel(DefaultModel, Timestamped):
    """
    Default app model that has `created_at` and `updated_at` attributes.
    """
    class Meta:
        abstract = True
