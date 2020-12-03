from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category

def home_page(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'blog/home_page.html', context)

def article_list(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'blog/article_list.html', context)

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    categories = Category.objects.all()
    context = {
        'article': article,
        'categories': categories
    }
    return render(request, 'blog/article_detail.html', context)

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
