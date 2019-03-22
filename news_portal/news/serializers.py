from rest_framework import serializers
from .models import Channel, Article

class ChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Channel
		fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = '__all__'
			