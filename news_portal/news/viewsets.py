from rest_framework import viewsets
from .models import Channel, Item
from .serializers import ChannelSerializer, ItemSerializer

class ChannelAll(viewsets.ModelViewSet):
	queryset = Channel.objects.all()
	serializer_class = ChannelSerializer

class ItemAll(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer		