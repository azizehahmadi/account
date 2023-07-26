from django.db import models



class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=300)
    short_description = models.TextField()
    text = models.TextField()
    is_active = models.BooleanField(default=True,)
    selected_categories = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, related_name='category_article')
    create_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comment')
    create_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()



    def __str__(self):
        return self.article.title