from article.models import Article, ArticleComment,ArticleCategory
from rest_framework import mixins, generics
from article.api.serializers import ArticleSerializer, ArticleCommentSerializer, ArticleCategorySerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class ArticleAV(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


    def get(self, request, *args , **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleDetailAV(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ArticleCommentAV(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):

    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentSerializer


    def get(self, request, *args , **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class ArticleCommentDetailAV(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             generics.GenericAPIView):
    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class ArticleCategoryAV(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):

    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer


    def get(self, request, *args , **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ArticleCategoryDetailAV(mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              generics.GenericAPIView):

    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class cat_article_comment(generics.ListAPIView):
    serializer_class = ArticleCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return ArticleComment.objects.filter(article=pk)

class cat_article_comment_create(generics.CreateAPIView):
    serializer_class = ArticleCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        article = Article.objects.get(pk=pk)
        serializer.save(article=article)