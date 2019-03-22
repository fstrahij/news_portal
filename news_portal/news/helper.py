from datetime import datetime
from bs4 import BeautifulSoup

class Helper(object):
	__imageLength = None
	__image = None			

	def __init__(self):
		super(Helper, self).__init__()

	def __setImageLength( self ):
		self.__imageLength = len(str( self.__image )) + 2

	def getImageSource( self, image ):
		self.__image = BeautifulSoup(image, "html.parser").find('img')
		self.__setImageLength()
		return self.__image['src']

	def getCleanText( self, someText ):
		return someText[self.__imageLength:]

	def getTimeDate( self, published ):
		return datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %z')