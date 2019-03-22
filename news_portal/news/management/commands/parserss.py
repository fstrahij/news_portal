from django.core.management.base import BaseCommand
from news.models import Channel, Article
from datetime import datetime
from bs4 import BeautifulSoup
import feedparser

class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		channels = { "news", "show", "sport", "tech" }
		channel = Channel()	
		article = Article()	
		#self.stdout.write("Prije:")
		for c in channels:			
			url = "https://www.24sata.hr/feeds/" + c + ".xml"
			feed = feedparser.parse(url)
			channel.title = feed["feed"]["title"]
			channel.link = feed["feed"]["link"]
			channel.description = feed["feed"]["description"]
			channel.language = feed["feed"]["language"]			
			channel.save()
			for i in feed.entries:
				article.title = i["title"]
				article.link = i["link"]
				image = BeautifulSoup(i["description"], "html.parser").find('img')
				article.image = image['src']
				start = len(str(image)) + 2
				article.description = i["description"][start:]
				article.pubDate = datetime.strptime(i.published, '%a, %d %b %Y %H:%M:%S %z')
				article.rss = url
				article.category = Channel.objects.get(title = i["category"])
				article.save()