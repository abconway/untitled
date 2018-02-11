import django_filters

from .models import Title


class TitleFilterSet(django_filters.FilterSet):
    class Meta:
        model = Title
        fields = ('id', 'name', 'slug', )
