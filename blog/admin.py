from django.contrib import admin
from blog.models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',) }

def make_publish_article(modeladmin, request, queryset):
    queryset.update(status='publish')
make_publish_article.short_description = 'انتشار مقالات انتخابی'

def make_article_in_slider(modeladmin, request, queryset):
    queryset.update(show_in_slider=True)
make_article_in_slider.short_description = 'نمایش مقالات انتخابی در اسلایدر'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',) }
    list_display = ('title', 'category', 'status', 'view_count', 'show_in_slider', 'created', 'updated')
    readonly_fields = ('view_count',)
    actions = (make_publish_article, make_article_in_slider)
    list_filter = ('status', 'show_in_slider')



