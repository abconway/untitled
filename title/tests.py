import json

from django.test import TestCase

from rest_framework.test import APIRequestFactory

from .models import Title
from .serializers import TitleSerializer
from .views import TitleViewSet


class TestTitleModel(TestCase):
    def test_default_ordering(self):
        first = Title.objects.create(name='First Title', slug='first-title')
        middle = Title.objects.create(name='Middle Title', slug='middle-title')
        last = Title.objects.create(name='Last Title', slug='Last-title')

        titles = Title.objects.all()

        self.assertEqual(last, titles[0])
        self.assertEqual(middle, titles[1])
        self.assertEqual(first, titles[2])


class TestTitleViewSet(TestCase):
    def test_filtering(self):
        Title.objects.create(name='Some Slug Here', slug='some-slug-here')
        Title.objects.create(name='Not Our Slug', slug='not-our-slug')

        factory = APIRequestFactory()
        request = factory.get('/api/titles/', {'slug': 'some-slug-here'})
        view = TitleViewSet.as_view({'get': 'list'})
        response = view(request)
        response.render()
        content = json.loads(response.content)

        self.assertEqual(len(content), 1)
        self.assertEqual(content[0]['name'], 'Some Slug Here')


class TestTitleSerializer(TestCase):
    def test_format(self):
        title = Title.objects.create(name='A Title', slug='a-title')
        data = TitleSerializer(title).data
        expected_data = {'id': 1, 'name': 'A Title', 'slug': 'a-title'}

        self.assertDictEqual(data, expected_data)
