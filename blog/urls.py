from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('articles/', views.article_list, name='article-list'),
    path('article/<str:slug>/', views.article_detail, name='article-detail'),
    path('category/<int:category_id>/<str:category_slug>/articles/', views.category_articles, name='category-articles'),
]