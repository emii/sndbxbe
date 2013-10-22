#-*- coding: utf-8 -*-
from datetime import date

AUTHOR = u'Emiliano Izquierdo'
SITENAME = u"//sndbx.be"
SITEURL = 'http://sndbx.be'
THEME = 'theme'
TIMEZONE = "Europe/Berlin"
PATH = 'contents/'
REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 10
DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'en'
RELATIVE_URLS = True
#PAGINATED_DIRECT_TEMPLATES = ['index']
#THEME_STATIC_PATHS = ['static']
#created css files for different proposes
CSS_FILE = 'style.css'
HIGHLIGHT_CSS_FILE = 'solarized_dark.css'
DECK_CSS_STYLE = 'sndbx.css'
#API key for google analytics
GA_ACCOUNT = 'UA-41003145-1'

#SOCIAL = (('twitter', 'http://twitter.com/emiizquierdo'),
#          ('8tracks', 'http://8tracks.com/emi'),
#          ('github', 'http://github.com/emii'),)

DEFAULT_CATEGORY = 'leftovers'
DEFAULT_DATE_FORMAT = '%d.%m.%Y'
#DISPLAY_PAGES_ON_MENU = False
#DISPLAY_CATEGORIES_ON_MENU = False
SUMMARY_MAX_LENGTH = 80
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
CATEGORY_URL = '{name}/'
CATEGORY_SAVE_AS = '{name}/index.html'
PAGE_DIR = 'pages'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CURRENT_DATE = date.today()
#some extensions to make sure pygments, anchors on headers and TOC work fine
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra','attr_list', 'headerid(forceid=False)','toc']
LOCALE = 'C'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
USE_FOLDER_AS_CATEGORY = False
ARTICLE_DIR = 'articles'
#static paths
THEME_STATIC_DIR = 'static'
THEME_STATIC_PATHS = ['static',]
OUTPUT_PATH = 'output/'
DELETE_OUTPUT_DIRECTORY = False
#folders to be copied to output static
STATIC_SAVE_AS = 'static/{path}'
STATIC_URL = 'static/{path}'
STATIC_PATHS = ['extra/robots.txt',
                'extra/favicon.ico',
                'images',
                'documents']
EXTRA_PATH_METADATA = {'extra/robots.txt':{'path':'../robots.txt'},'extra/favicon.ico':{'path':'../favicon.ico'},}
#plugins
PLUGIN_PATH = "plugins"
PLUGINS = ["pelican_references",]#"pelican_gallery","pelican_thumbnailer"]
#enable fancybox for galleries
ENABLE_FANCYBOX = True
#implementation for image galleries
IMAGE_PATH = "images/gallery"
THUMBNAIL_DIR = "static/images/thumbnails"
THUMBNAIL_SIZES = {'thumbnail_wide' : '200x?'}
#PAGINATION_PATTERNS = ((1, '{base_name}/', '{base_name}/index.html'), (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'), )
