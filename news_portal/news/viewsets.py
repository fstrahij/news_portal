from rest_framework import serializers
from .models import Channel, Item
from .serializers import ChannelSerializer, ItemSerializer

class ChannelViewSet(viewsets.ModelViewSet):
	queryset = Channel.objects.all()
	serializer_class = ChannelSerializer

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
		