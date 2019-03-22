from rest_framework import viewsets, filters, generics
from .models import Channel, Article
from .serializers import ChannelSerializer, ArticleSerializer

class Channels(viewsets.ModelViewSet):
	queryset = Channel.objects.all()
	serializer_class = ChannelSerializer

class Articles(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('description', 'title')	
	def get_queryset(self):	
		queryset = Article.objects.all()
		user_category = self.request.query_params.get('category')
		if user_category is not None:
			queryset = Article.objects.filter(category = user_category)		
		return queryset.order_by('-pubDate')	
		