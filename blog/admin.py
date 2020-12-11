from django.contrib import admin
from blog.models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',) }


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',) }
    readonly_fields = ('view_count',)



