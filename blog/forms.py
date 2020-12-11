from django import forms
from django.db.models import fields
from blog.models import Article


class CategoryForm(forms.Form):
    title = forms.CharField(max_length=150)
    slug = forms.CharField(max_length=150)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = ('title', 'slug', 'author', 'categories', 'body', 'thumbnail', 'status')
        # fields = '__all__'
        exclude = ('view_count',)
