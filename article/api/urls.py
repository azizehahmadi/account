from django.urls import path
from article.api.views import ArticleAV, \
    ArticleCategoryAV, ArticleCommentAV, ArticleCategoryDetailAV,\
    ArticleDetailAV, \
    ArticleCommentDetailAV, cat_article_comment, cat_article_comment_create

urlpatterns = [
    path('list/', ArticleAV.as_view(), name='article_list'),
    path('list/<int:pk>/', ArticleDetailAV.as_view(), name='article_list_detail'),


    path('category/', ArticleCategoryAV.as_view(), name='article_category'),
    path('category/<int:pk>/', ArticleCategoryDetailAV.as_view(), name='article_category_detail'),


    path('comment/', ArticleCommentAV.as_view(), name='article_comment'),
    path('comment/<int:pk>/', ArticleCommentDetailAV.as_view(), name='article_comment_detail'),

    path('category/<int:pk>/article-comment/', cat_article_comment.as_view(), name='cat-comment'),
    path('category/<int:pk>/article-comment-create/', cat_article_comment_create.as_view(), name='cat-comment-create')


]
