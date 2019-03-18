from django.db import models
# Create your models here.
class Channel(models.Model):
	title = models.CharField(max_length = 30, primary_key = True)
	link = models.URLField()
	description = models.TextField(null = True)
	language = models.CharField(max_length = 10)
	lastBuildDate = models.DateTimeField()

class Item(models.Model):
	title = models.CharField(max_length = 30, primary_key = True)
	link = models.URLField()
	description = models.TextField()
	image = models.ImageField(blank = True, null = True)
	language = models.CharField(max_length = 10)
	pubDate = models.DateTimeField()
	guid = models.URLField()
	category = models.ForeignKey(Channel, on_delete = models.CASCADE)