from datetime import datetime
from bs4 import BeautifulSoup

class Helper:
	__imageLength = None
	__image = None			
	__fullText = None

	@classmethod
	def __setImageLength( self ):
		self.__imageLength = len(str( self.__image )) + 2

	@classmethod	
	def getImageSource( self, image ):		
		self.__fullText = image
		self.__image = BeautifulSoup(image, "html.parser").find('img')
		self.__setImageLength()
		return self.__image['src']

	@classmethod	
	def getCleanText( self ):
		return self.__fullText[self.__imageLength:]

	@classmethod	
	def getTimeDate( self, published ):
		return datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %z')