from rest_framework import serializers
from article.models import ArticleComment, ArticleCategory, Article


class ArticleCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleComment
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):

    article_comment = ArticleCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = "__all__"



class ArticleCategorySerializer(serializers.ModelSerializer):

    article = ArticleSerializer(many=True, read_only=True, source='category_article')

    class Meta:
        model = ArticleCategory
        fields = ('id', 'parent', 'title', 'is_active', 'article',)






