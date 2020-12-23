from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from blog.models import Article, Category
from .forms import CategoryForm, ArticleForm
from django.template.defaultfilters import slugify
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

def category_articles(request, category_id, category_slug):
    categories = Category.objects.all()
    category = categories.get(id=category_id, slug=category_slug)
    articles = category.articles.all()
    context = {
        'categories': categories,
        'category': category,
        'articles': articles
    }
    return render(request, 'blog/category_articles.html', context)

def article_detail(request, id):
    # article = Article.objects.get(id=id)
    article = get_object_or_404(Article, id=id, status='publish')
    article.view_count += 1
    article.save()
    article.refresh_from_db()
    return render(request, '', {'article': article})

class HomeTemplateView(TemplateView):
    template_name = 'blog/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.published()
        # context['categories'] = Category.objects.all()
        return context

class ArticleListView(ListView):
    # model = Article
    queryset = Article.objects.published()
    # template_name = 'blog/article_list.html'
    # template_name = '{app}/{model}_list.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context 

class CategoryListView(ListView):
    model = Category

class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.status == 'publish':
            self.object.view_count += 1
            self.object.save()
            self.object.refresh_from_db()
        context['categories'] = Category.objects.all()
        return context 

class CategoryDetailView(DetailView):
    model = Category

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context 

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('blog:article-list')

class ArticleUpdateView(UpdateView):
    model = Article
    fields = '__all__'
    success_url = reverse_lazy('blog:article-list')

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:article-list')








