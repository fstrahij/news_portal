from django.db import models
# Create your models here.
class Channel(models.Model):
	title = models.CharField(max_length = 30, primary_key = True)
	link = models.URLField()
	description = models.TextField(null = True)
	language = models.CharField(max_length = 10)

class Item(models.Model):
	title = models.CharField(max_length = 30, primary_key = True)
	link = models.URLField()
	description = models.TextField()
	pubDate = models.CharField(max_length = 100)
	rss = models.URLField()
	category = models.ForeignKey(Channel, on_delete = models.CASCADE)