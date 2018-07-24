#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Paul D. Mendes'
SITENAME = "Careful Considerations"
BANNER = 'theme/images/universe-1351865_1920.jpg'
BANNER_SUBTITLE = 'A Page For Anything I Feel Like'
# AVATAR = 'theme/images/me400x400.png'#{photo}admin-ajax.php_400x400.png'
# ABOUT_ME = 'Hi'
SITEURL = ''#'https://grilledchickenthighs.github.io'
TIMEZONE = 'America/New_York'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_LANG = 'en'
BOOTSTRAP_FLUID = True
DEFAULT_PAGINATION = 3
NEWEST_FIRST_ARCHIVES = True
# REVERSE_CATEGORY_ORDER = True

# Developoing Settings
DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = False
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Paths
PATH = 'content'
PAGE_PATHS = ['pages','index']
STATIC_PATHS = ['images','pdfs','extra'] # # TODO: Add cv under pdf
# EXTRA_PATH_METADATA = {
#     # 'extra/custom.css': {'path': 'custom.css'},
#     # 'extra/robots.txt': {'path': 'robots.txt'},
#     # 'extra/favicon.ico': {'path': 'favicon.ico'},
#     'extra/CNAME': {'path': 'CNAME'},
#     'extra/LICENSE': {'path': 'LICENSE'},
# }

# Extra Custom JS, CSS
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'},
    'extra/README.md': {'path': 'README.md'}
}

ARTICLE_PATHS = ['posts', 'notebooks']
DISPLAY_ARTICLE_INFO_ON_INDEX = False

MARKUP = ('md', 'ipynb')
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
PLUGIN_PATHS = ['./pelican-plugins','./plugins']
#What a headache https://github.com/getpelican/pelican-themes/issues/460
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'

PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'tipue_search',
    'render_math',
    'summary',
    'ipynb.markup']

# Ignore ipython css and use theme pygments
IPYNB_IGNORE_CSS= True
# IPYNB_FIX_CSS = True
IPYNB_GENERATE_SUMMARY = True
# CATEGORY_SAVE_AS = ''
# for Tique Search Plugin
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')

# Url Image
FAVICON = 'theme/images/272264-2T92_big.png'
SITELOGO = 'theme/images/272264-2T92_big.png'
SITELOGO_SIZE = 33
HIDE_SITENAME = True

# Top menus
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_ARTICLE_INFO_ON_INDEX = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


SHOW_ARTICLE_AUTHOR = False

# Sidebar Options
# PAGE_SINGLE_COLUMN_STYLE = True
# PAGE_HIDE_SIDEBAR = False
# PADDED_SINGLE_COLUMN_STYLE = False
HIDE_SIDEBAR = True
# SIDEBAR_ON_LEFT = True
DISABLE_SIDEBAR_TITLE_ICONS = True
DISPLAY_ARCHIVE_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_TAGS_INLINE = True
# DISPLAY_SERIES_ON_SIDEBAR = True
# SHOW_SERIES = True
# DISPLAY_BREADCRUMBS = True

# Blogroll
# LINKS = (('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/GrilledChickenThighs'),
          ('Linkedin', 'https://www.linkedin.com/in/paul-mendes'),)
GITHUB_USER = "grilledchickenthighs"
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True
