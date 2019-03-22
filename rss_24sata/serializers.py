from .models import Category, Article
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Category
    fields = ('url', 'id', 'name')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Article
    fields = ('url', 'id', 'channel', 'title', 'description', 'link', 'date_posted')
