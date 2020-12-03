# Generated by Django 3.1.3 on 2020-11-29 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان دسته\u200cبندی')),
                ('slug', models.SlugField(allow_unicode=True, max_length=150, unique=True, verbose_name='لینک یکتا')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_categories', to='blog.category', verbose_name='دسته\u200cبندی سطح بالا')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته\u200cبندی\u200cها',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان مقاله')),
                ('slug', models.SlugField(allow_unicode=True, max_length=150, unique=True, verbose_name='لینک یکتا')),
                ('body', models.TextField(verbose_name='متن مقاله')),
                ('thumbnail', models.ImageField(default='01.png', upload_to='', verbose_name='تصویر شاخص')),
                ('status', models.CharField(default='draft', max_length=15, verbose_name='وضعیت انتشار')),
                ('view_count', models.IntegerField(default=0, verbose_name='تعداد بازدید')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='blog.category', verbose_name='دسته\u200cبندی')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقاله\u200cها',
                'ordering': ('created',),
            },
        ),
    ]