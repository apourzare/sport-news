from django import forms
from blog.models import Article, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('parent', 'created', 'updated')


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('view_count',)
