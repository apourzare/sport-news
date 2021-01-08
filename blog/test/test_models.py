from django.test import TestCase, Client
from ..models import Category


class TestModel(TestCase):
    def test_category_create(self):
        category = Category.objects.create(title='test slug')

        self.assertEqual(category.slug, 'test-slug')
