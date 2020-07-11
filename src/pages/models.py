from app.models import TimestampedModel, models


class Page(TimestampedModel):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
