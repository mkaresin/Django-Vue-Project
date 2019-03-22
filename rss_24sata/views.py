from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import ArticleSerializer, CategorySerializer
from .models import Article, Category


class ArticleViewSet(viewsets.ModelViewSet):
  queryset = Article.objects.get_queryset().order_by('id')
  serializer_class = ArticleSerializer
  pagination_class = PageNumberPagination
  http_method_names = ['get', 'head']


class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.get_queryset().order_by('id')
  serializer_class = CategorySerializer
  pagination_class = PageNumberPagination
  http_method_names = ['get', 'head']

  @action(detail=True)
  def articles(self, request, pk):
    categ = self.get_object()
    art_set = Article.objects.filter(category=categ).order_by('id')
    paginator = PageNumberPagination()
    art_set = paginator.paginate_queryset(art_set, request, view=ArticleViewSet)
    serializer = ArticleSerializer(art_set, many=True, context={'request': request})
    return Response(serializer.data)
