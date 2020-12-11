from django.db import models
from accounts.models import User
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان دسته‌بندی')
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True, verbose_name='لینک یکتا')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='دسته‌بندی سطح بالا', related_name='sub_categories')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'
        ordering = ('created',)
        db_table = 'category'

    def __str__(self):
        return self.title


class Article(models.Model):
    PUBLISH_STATUS = (
        ('draft', 'پیش‌نویس'),
        ('publish', 'انتشار‌یافته'),
        ('archive', 'بایگانی‌شده'),
    ) 
    title = models.CharField(max_length=150, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True, verbose_name='لینک یکتا')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', related_name='articles')
    categories = models.ManyToManyField(Category, verbose_name='دسته‌بندی‌ها', related_name='articles')
    body = models.TextField(verbose_name='متن مقاله')
    thumbnail = models.ImageField(upload_to='articles/%y/%m/', verbose_name='تصویر شاخص', default='01.png')
    status = models.CharField(max_length=15, verbose_name='وضعیت انتشار', choices=PUBLISH_STATUS, default='draft')
    view_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')


    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله‌ها'
        ordering = ('created',)
        db_table = 'article'
        
    def __str__(self):
        return self.title

    # def save(self):
    #     pass


# article = Article.objects.get(condition)
# article.author

# author = User.objects.get(condition)
# author_articles = author.articles.all()

# author = User.objects.get(username=apourzare)
# articles = Article.objects.filter(author=arthor)

# tag = Tag.objects.get(condition)
# article = Article.objects.get(condition)
# tags = article.tags.all()
# tags.count()
# categories = categories.categories.all()


# articles = tag.article.all()
# tags = article.tag.all()