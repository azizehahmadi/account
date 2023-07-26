from django.contrib import admin
from article.models import ArticleCategory, Article, ArticleComment
# Register your models here.

admin.site.register(ArticleCategory)
admin.site.register(Article)
admin.site.register(ArticleComment)