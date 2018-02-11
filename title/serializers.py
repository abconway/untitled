from rest_framework.serializers import ModelSerializer

from .models import Title


class TitleSerializer(ModelSerializer):
    class Meta:
        model = Title
        fields = ('id', 'name', 'slug',)
