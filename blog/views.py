from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Category
from .forms import CategoryForm, ArticleForm
from django.template.defaultfilters import slugify

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
    # article = Article.objects.get(slug=slug)
    article = get_object_or_404(Article, slug=slug)
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

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # category = Category(title=cd['title'], slug=cd['slug'])
            category = Category(title=cd['title'])
            if cd['slug']:
                category.slug = slugify(cd['slug'])
            else:
                category.slug = slugify(cd['title'])
            category.save()
            return redirect('blog:article-list')
    else:
        form = CategoryForm()
        categories = Category.objects.all()
        return render(request, 'blog/add_category.html', {'form': form, 'categories': categories})

def add_article(request):
    if request.method == 'POST':
        pass
    else:
        form = ArticleForm()
        categories = Category.objects.all()
        return render(request, 'blog/add_article.html', {'form': form, 'categories': categories})