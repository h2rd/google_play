import re
import urllib

from lxml import html
from grab.selector import XpathSelector

import requests

CATEGORIES = [
    "application", "app_wallpaper", "app_widgets", "arcade",
    "books_and_reference", "brain", "business", "cards",
    "casual", "comics", "communication", "education",
    "entertainment", "finance", "game", "game_wallpaper",
    "game_widgets", "health_and_fitness", "libraries_and_demo", "lifestyle",
    "media_and_video", "medical", "music_and_audio", "news_and_magazines",
    "personalization", "photography", "productivity", "racing",
    "shopping", "social", "sports", "sports_games",
    "tools", "transportation", "travel_and_local", "weather"
]

FREE = 'topselling_free'
PAID = 'topselling_paid'

def _get_apps(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None

    doc = html.fromstring(r.content)

    apps = []
    for elem in doc.xpath('//div[@class="card-list"]/div[@data-docid]'):
        apps.append(elem.attrib['data-docid'])

    return apps


def leaderboard(identifier, category=None, start=0,
                num=24, hl="en"):
    if identifier not in ('topselling_paid', 'topselling_free'):
        raise Exception("identifier must be topselling_paid or topselling_free")

    url = 'https://play.google.com/store/apps'
    if category:
        if category not in CATEGORIES:
            raise Exception('%s not exists in category list' % category)
        url += "/category/" + str(category).upper()

    url += "/collection/%s?start=%s&num=%s&hl=%s" % (identifier, start, num, hl)

    return _get_apps(url)


def search(query, start=0, num=24, hl="en"):
    url = ('https://play.google.com/store/search'
           '?q=%s&start=%s&num=%s&hl=%s') % (query, start, num, hl)

    return _get_apps(url)


def developer(developer, start=0, num=24, hl="en"):
    url = ('https://play.google.com/store/apps/developer'
           '?id=%s&start=%s&num=%s&hl=%s') % (urllib.quote_plus(developer), start, num, hl)

    return _get_apps(url)


def app(package_name, hl='en'):
    package_url = ("https://play.google.com/store/apps/details"
                   "?id=%s&hl=%s") % (package_name, hl)

    r = requests.get(package_url)
    if r.status_code != 200:
        return None

    doc = XpathSelector(html.fromstring(r.content))

    app = dict()
    app['title'] = doc.select('//div[@class="document-title"]').text()
    app['url'] = package_url
    app['package_name'] = package_name
    app['description'] = "\n".join(doc.select('//div[@class="id-app-orig-desc"]').text_list())
    app['category'] = doc.select('//span[@itemprop="genre"]').text()
    app['logo'] = doc.select('//img[@class="cover-image"]').attr('src')
    app['price'] = doc.select('//meta[@itemprop="price"]').attr('content')
    app['developer_name'] = doc.select('//div[@itemprop="author"]/a').text()
    try:
        developer_email = doc.select('//a[starts-with(@href, "mailto")]').attr('href')[7:]
    except:
        developer_email = ''
    app['developer_email'] = developer_email
    developer_website = re.search('\?q=(.*)&sa', doc.select('//a[@class="dev-link"]').attr('href'))
    if developer_website:
        app['developer_website'] = developer_website.group(1) or ''
    else:
        app['developer_website'] = ''
    app['rating'] = float(doc.select('//div[@class="score"]').text())
    app['reviews'] = int(doc.select('//span[@class="reviews-num"]').text().replace(',', ''))
    app['version'] = doc.select('//div[@itemprop="softwareVersion"]').text()
    app['size'] = doc.select('//div[@itemprop="fileSize"]').text()
    try:
        installs = doc.select('//div[@itemprop="numDownloads"]').text()
    except:
        installs = ''
    app['installs'] = installs
    app['android'] = doc.select('//div[@itemprop="operatingSystems"]').text()
    app['images'] = [im.attr('src') for im in doc.select('//img[@itemprop="screenshot"]')]
    app['similar'] = [item.attr('data-docid')
                      for item in doc.select('//div[@class="rec-cluster"][1]/*/div[@data-docid]')]
    return app
