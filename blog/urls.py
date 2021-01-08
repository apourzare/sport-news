from django.urls import path
from . import views
from . import api_views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('articles/', views.ArticleListView.as_view(), name='article-list'),
    path('article/insert/', views.ArticleCreateView.as_view(), name='add-article'),
    path('article/<str:slug>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article-delete'),
    path('categories/', views.CategoryListView.as_view(), name='categories-list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='add-category'),
    path('category/<int:pk>/<str:slug>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/<int:category_id>/<str:category_slug>/articles/', views.category_articles, name='category-articles'),
    path('api/categories/', api_views.CategoryListAPIView.as_view()),
    path('api/category/<int:pk>/', api_views.CategoryRetrieveAPIView.as_view()),
    path('api/category/create/', api_views.CategoryCreateAPIView.as_view()),
    path('api/category/<int:pk>/update/', api_views.CategoryUpdateAPIView.as_view()),
    path('api/category/<int:pk>/delete/', api_views.CategoryDestroyAPIView.as_view()),
    path('api/v2/categories/', api_views.CategoryListCreateAPIView.as_view()),
    path('api/v2/categories/<int:pk>/', api_views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('api/articles/', api_views.ArticleList.as_view()),
    path('api/article/<int:pk>/', api_views.ArticleDetail.as_view()),

]