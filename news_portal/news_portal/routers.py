from rest_framework import routers
from news import viewsets

router = routers.DefaultRouter()

router.register(r'channels', viewsets.ChannelAll)
router.register(r'articles', viewsets.ArticleAll)