from rest_framework.viewsets import ModelViewSet

from .models import Title
from .serializers import TitleSerializer


class TitleViewSet(ModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()

