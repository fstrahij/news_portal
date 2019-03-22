from rest_framework import viewsets, filters
from .models import Channel, Article
from .serializers import ChannelSerializer, ArticleSerializer

class ChannelAll(viewsets.ModelViewSet):
	queryset = Channel.objects.all()
	serializer_class = ChannelSerializer

class ArticleAll(viewsets.ModelViewSet):
	queryset = Article.objects.all().order_by('-pubDate')
	serializer_class = ArticleSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('description', 'title')