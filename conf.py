#-*- coding: utf-8 -*-
from datetime import date

AUTHOR = u'Emiliano Izquierdo'
SITENAME = u"//sndbx.be"
SITEURL = 'http://sndbx.be'
THEME = 'theme'
TIMEZONE = "America/Mexico_City"
PATH = 'contents/'
REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 10
DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'en'
RELATIVE_URLS = True
OUTPUT_PATH = 'output/'
DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS = ['images']
PAGINATED_DIRECT_TEMPLATES = ('index',)
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'style.css'

SOCIAL = (('twitter', 'http://twitter.com/emiizquierdo'),
          ('8tracks', 'http://8tracks.com/emi'),
          ('github', 'http://github.com/emii'),)

DEFAULT_CATEGORY = 'leftovers'
DEFAULT_DATE_FORMAT = '%d.%m.%Y'
DISPLAY_PAGES_ON_MENU = False
SUMMARY_MAX_LENGTH = 80
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
CATEGORY_URL = '{name}/'
CATEGORY_SAVE_AS = '{name}/index.html'
PAGE_DIR = 'pages'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CURRENT_DATE=date.today()
MD_EXTENSIONS = ['codehilite','extra']
LOCALE = 'C'









