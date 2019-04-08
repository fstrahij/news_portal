from django.db import models
# Create your models here.
class Channel(models.Model):
	title = models.CharField(max_length = 30, primary_key = True)
	link = models.URLField()
	description = models.TextField(null = True)
	language = models.CharField(max_length = 10)

class Article(models.Model):
	title = models.CharField(max_length = 100)
	link = models.URLField(primary_key = True)
	image = models.TextField()
	description = models.TextField()
	pubDate = models.DateTimeField()
	rss = models.TextField()
	category = models.CharField(max_length = 30)