from django.core.management.base import BaseCommand
from datetime import datetime
from urllib.request import urlopen
from rss_24sata.models import Category, Article
import xmltodict


def store_to_db(rss_source):
  category = Category(name=rss_source['rss']['channel']['title'])
  category.save()
  item = rss_source['rss']['channel']['item']

  for i in item:

    date_string = i['pubDate']
    dt_obj = datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %z')

    art = Article(title=i['title'], date_posted=dt_obj, description=i['description'], link=i['link'], channel=category)
    art.save()
    art.category.add(category)
  return


class Command(BaseCommand):

  help = 'Parse xml data from url'

  rss_dict = {

      'aktualno': "http://www.24sata.hr/feeds/aktualno.xml",
      'news': "http://www.24sata.hr/feeds/news.xml",
      'sport': "http://www.24sata.hr/feeds/sport.xml",
      'tech': "http://www.24sata.hr/feeds/tech.xml",

  }

  def handle(self, *args, **kwargs):

    Article.objects.all().delete()
    Category.objects.all().delete()

    for link in Command.rss_dict.values():
      channel = urlopen(link)
      channel = channel.read()
      channel = xmltodict.parse(channel)
      store_to_db(channel)

    self.stdout.write("RSS Data is successfully parsed")
