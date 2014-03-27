import re
import urllib

from bs4 import BeautifulSoup
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

    apps = []
    soup = BeautifulSoup(r.content, "lxml")
    for elem in soup.find_all('div', 'card'):
        apps.append(elem.attrs['data-docid'])

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

    soup = BeautifulSoup(r.content, "lxml")

    app = dict()
    app['title'] = soup.find('div', 'document-title').text.strip()
    app['url'] = package_url
    app['package_name'] = package_name
    app['description'] = soup.find('div', 'id-app-orig-desc').text.strip()
    app['category'] = soup.find('span', itemprop='genre').text
    app['logo'] = soup.find('img', "cover-image").attrs['src']
    app['price'] = soup.find('meta', itemprop="price").attrs['content']
    app['developer_name'] = soup.find('div', itemprop="author").a.text.strip()
    try:
        app['developer_email'] = soup.find('a', href=re.compile("^mailto")).attrs['href'][7:]
    except:
        app['developer_email'] = ''

    link = soup.find('a', "dev-link").attrs['href']
    developer_website = re.search('\?q=(.*)&sa', link)
    if developer_website:
        app['developer_website'] = developer_website.group(1) or ''
    else:
        app['developer_website'] = ''

    app['rating'] = float(soup.find('div', 'score').text)
    app['reviews'] = int(soup.find('span', 'reviews-num').text.replace(',', ''))
    app['version'] = soup.find('div', itemprop="softwareVersion").text.strip()
    app['size'] = soup.find('div', itemprop="fileSize").text.strip()

    try:
        app['installs'] = soup.find('div', itemprop="numDownloads").text.strip()
    except:
        app['installs'] = ''

    app['android'] = soup.find('div', itemprop="operatingSystems").text.strip()
    app['images'] = [im.attrs['src']
                     for im in soup.find_all('img', itemprop="screenshot")]

    html = soup.find('div', "rec-cluster")
    if html:
        app['similar'] = [similar.attrs['data-docid']
                          for similar in html.find_all('div', 'card')]
    else:
        app['similar'] = []

    return app
