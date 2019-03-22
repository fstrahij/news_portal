from rest_framework import viewsets, filters
from .models import Channel, Item
from .serializers import ChannelSerializer, ItemSerializer

class ChannelAll(viewsets.ModelViewSet):
	queryset = Channel.objects.all()
	serializer_class = ChannelSerializer

class ItemAll(viewsets.ModelViewSet):
	queryset = Item.objects.all().order_by('-pubDate')
	serializer_class = ItemSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('description', 'title')