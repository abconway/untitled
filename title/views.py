from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .filters import TitleFilterSet
from .models import Title
from .serializers import TitleSerializer


class TitleViewSet(ModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, )
    filter_class = TitleFilterSet
