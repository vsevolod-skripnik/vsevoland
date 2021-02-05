from django.db import models

from default.models import DefaultModel


class Comic(DefaultModel):
    slug = models.SlugField()

    owner = models.ForeignKey(
        'users.User',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='comics',
    )

    def __str__(self):
        return self.slug
