from random import choices
from string import ascii_lowercase

from django.db import models
from django_extensions.db.models import TimeStampedModel, AutoSlugField


class CustomAutoSlugField(AutoSlugField):
    def slug_generator(self, original_slug, start):
        yield original_slug
        for i in range(start, self.max_unique_query_attempts):
            slug = original_slug
            random_five_character_string = ''.join(choices(ascii_lowercase, k=5))
            end = '%s%s' % (self.separator, random_five_character_string)
            end_len = len(end)
            if self.slug_len and len(slug) + end_len > self.slug_len:
                slug = slug[:self.slug_len - end_len]
                slug = self._slug_strip(slug)
            slug = '%s%s' % (slug, end)
            yield slug
        raise RuntimeError('max slug attempts for %s exceeded (%s)' % (original_slug, self.max_unique_query_attempts))


class Title(TimeStampedModel):
    name = models.CharField(max_length=4096, null=False, blank=False)
    slug = CustomAutoSlugField(populate_from='name')
