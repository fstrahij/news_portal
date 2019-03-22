from django.core.management.base import BaseCommand
from news.models import Channel, Article
from news.helper import Helper
import feedparser

class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		channels = { "news", "show", "sport", "tech" }
		channel = Channel()	
		article = Article()	
		helper = Helper()
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
				article.image = helper.getImageSource( i["description"] )
				article.description = helper.getCleanText( i["description"] )
				article.pubDate = helper.getTimeDate( i.published )
				article.rss = url
				article.category = i["category"]
				article.save()