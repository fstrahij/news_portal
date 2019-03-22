from django.core.management.base import BaseCommand
from news.models import Channel, Item
from datetime import datetime
from bs4 import BeautifulSoup
import feedparser

class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		channels = { "news", "show", "sport", "tech" }
		channel = Channel()	
		item = Item()	
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
				item.title = i["title"]
				item.link = i["link"]
				image = BeautifulSoup(i["description"], "html.parser").find('img')
				item.image = image['src']
				start = len(str(image)) + 2
				item.description = i["description"][start:]
				item.pubDate = datetime.strptime(i.published, '%a, %d %b %Y %H:%M:%S %z')
				item.rss = url
				item.category = Channel.objects.get(title = i["category"])
				item.save()