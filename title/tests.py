import random

from django.test import TestCase

from .models import Title


class TestTitleModel(TestCase):
    def test_slugification(self):
        random.seed(555)
        name = 'I am a title'

        first_title = Title.objects.create(name=name)
        self.assertEqual(first_title.name, name)

        first_expected_slug = 'i-am-a-title'
        self.assertEqual(first_title.slug, first_expected_slug)

        second_title = Title.objects.create(name=name)
        self.assertEqual(second_title.name, name)
        self.assertNotEqual(first_title.slug, second_title.slug)

        second_expected_slug = 'i-am-a-title-feoxd'
        self.assertEqual(second_title.slug, second_expected_slug)
