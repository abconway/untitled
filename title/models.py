from django.db import models
from django_extensions.db.models import TimeStampedModel


class Title(TimeStampedModel):
    class Meta:
        ordering = ['-modified']

    name = models.CharField(max_length=4096, null=False, blank=False)
    slug = models.SlugField(max_length=4096, null=False, blank=False)
