from django.template.defaultfilters import slugify
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Category, Article
from ..forms import CategoryForm, ArticleForm


class CategoryTestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_category_add_POST_valid(self):
        response = self.client.post(reverse('blog:add-category'), data={
            'title': 'دوچرخه سواری',
            'slug': 'دوچرخه-سواری'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Category.objects.count(), 1)

    def test_category_add_POST_invalid(self):
        response = self.client.post(reverse('blog:add-category'), data={
            'title': 'دوچرخه سواری'
        })
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(response, 'form', field='slug', errors='این مقدار لازم است.')


class ArticleTestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_article_add_GET(self):
        response = self.client.get(reverse('blog:add-article'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article_form.html')
        self.failUnless(response.context['form'], ArticleForm)


