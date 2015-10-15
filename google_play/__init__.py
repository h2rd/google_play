import re
import urllib
import lxml.html
import requests

from bs4 import UnicodeDammit


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


def decode_html(html_string):
    converted = UnicodeDammit(html_string)

    if not converted.unicode_markup:
        raise UnicodeDecodeError(
                "Failed to detect encoding, tried [%s]",
                ', '.join(converted.triedEncodings))

    return converted.unicode_markup


def _get_text(doc, sel, default=''):
    els = doc.cssselect(sel)
    if len(els) > 0:
        return unicode(els[0].text_content()).strip()
    else:
        return default or ''


def _get_attrs(doc, sel, attr):
    return [el.get(attr) for el in doc.cssselect(sel)]


def _get_apps(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None

    doc = lxml.html.fromstring(decode_html(r.content))
    apps = _get_attrs(doc, 'div.card', 'data-docid')

    return apps


def leaderboard(identifier, category=None, start=0, num=24, hl="en"):
    if identifier not in ('topselling_paid', 'topselling_free'):
        raise Exception("identifier must be topselling_paid or topselling_free")

    url = 'https://play.google.com/store/apps'
    if category:
        if category not in CATEGORIES:
            raise Exception('%s not exists in category list' % category)
        url += "/category/" + str(category).upper()

    url += "/collection/%s?start=%s&num=%s&hl=%s" % (identifier, start, num, hl)
    return _get_apps(url)


def search(query, hl="en", c="apps"):
    url = ('https://play.google.com/store/search'
           '?q=%s&hl=%s&c=%s') % (query, hl, c)
    return _get_apps(url)


def developer(developer, num=24, hl="en", c="apps"):
    url = ('https://play.google.com/store/apps/developer'
           '?id=%s&num=%s&hl=%s&c=%s') % (
                   urllib.quote_plus(developer), num, hl, c)
    return _get_apps(url)


def app(package_name, hl='en', c="apps"):
    package_url = ("https://play.google.com/store/apps/details"
                   "?id=%s&hl=%s&c=%s") % (package_name, hl, c)

    r = requests.get(package_url)
    if r.status_code != 200:
        return None

    doc = lxml.html.fromstring(decode_html(r.content))

    developer_website = re.search('\?q=(.*)&sa',
            _get_attrs(doc, 'a.dev-link', 'href')[0])

    if developer_website:
        developer_website = developer_website.group(1) or ''
    else:
        developer_website = ''

    return dict(
        title=_get_text(doc, 'h1.document-title'),
        url=package_url,
        package_name=package_name,
        description=_get_text(doc, 'div.id-app-orig-desc'),
        category=_get_text(doc, 'span[itemprop=genre]'),
        logo=_get_attrs(doc, 'img.cover-image', 'src')[0],
        price=_get_attrs(doc, 'meta[itemprop="price"]', 'content')[0],
        developer_name=_get_text(doc, 'div[itemprop="author"] span[itemprop="name"]'),
        developer_email=_get_attrs(doc, 'a.dev-link[href^=mailto]', 'href')[0][7:],
        developer_website=developer_website,
        rating=float(_get_text(doc, 'div.score')),
        reviews=int(_get_text(doc, 'span.reviews-num').replace(',', '')),
        version=_get_text(doc, 'div[itemprop="softwareVersion"]'),
        size=_get_text(doc, 'div[itemprop=fileSize]'),
        installs=_get_text(doc, 'div[itemprop=numDownloads]'),
        android=_get_text(doc, 'div[itemprop=operatingSystems]'),
        images=_get_attrs(doc, 'img[itemprop="screenshot"]', 'src'),
        similar=_get_attrs(doc, 'div.card', 'data-docid')
    )
