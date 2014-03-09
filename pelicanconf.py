#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Katie Green'
SITENAME = u'Data in the Rough'
SITETAGLINE = u'Exploring data science and visualization'
SITEURL = ''
SITELOGO = 'logo8.png'


LINKEDIN_URL = 'http://www.linkedin.com/pub/katie-green/12/651/70a'
TWITTER_URL = 'https://twitter.com/katiefg28'

TIMEZONE = 'Europe/Helsinki'
DATE_FORMATS = {'en': '%b %d,  %Y'}
DEFAULT_LANG = u'en'
SUMMARY_MAX_LENGTH = 75


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10
THEME = 'pelican-themes/lannisport-master'
OUTPUT_PATH = 'output'
PATH = 'content'
STATIC_PATHS = [
    'files',
    'images',
    'resume'
]

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'


DEFAULT_PAGINATION = 10
OUTPUT_PATH = 'output'
PATH = 'content'



# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
