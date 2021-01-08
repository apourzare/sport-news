from django.db import models
from django.template.defaultfilters import slugify
from accounts.models import User
from .managers import CategoryManager, ArticleManager


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان دسته‌بندی')
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True, verbose_name='لینک یکتا')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                               verbose_name='دسته‌بندی سطح بالا', related_name='sub_categories')
    status = models.BooleanField(default=False, verbose_name='وضعیت')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'
        ordering = ('-created',)
        db_table = 'category'

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        # if self.slug is None:
        self.slug = slugify(self.title)
        super(Category, self).save(**kwargs)

    objects = CategoryManager()


class Article(models.Model):
    PUBLISH_STATUS = (
        ('draft', 'پیش‌نویس'),
        ('publish', 'انتشار‌یافته'),
        ('archive', 'بایگانی‌شده'),
    ) 
    title = models.CharField(max_length=150, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True, verbose_name='لینک یکتا')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='نویسنده',
                               related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='دسته‌بندی‌ها',
                                 related_name='articles')
    body = models.TextField(verbose_name='متن مقاله')
    thumbnail = models.ImageField(upload_to='articles/%y/%m/', null=True, blank=True, verbose_name='تصویر شاخص',
                                  default='01.png')
    status = models.CharField(max_length=15, verbose_name='وضعیت انتشار', choices=PUBLISH_STATUS, default='draft')
    view_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    show_in_slider = models.BooleanField(default=False, verbose_name='نمایش در اسلایدر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله‌ها'
        ordering = ('-created',)
        db_table = 'article'
        
    def __str__(self):
        return self.title

    def save(self, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Article, self).save(**kwargs)

    objects = ArticleManager()




