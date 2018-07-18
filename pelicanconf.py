#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Paul D. Mendes'
SITENAME = "Paul D. Mendes"
SITEURL = ''#'https://grilledchickenthighs.github.io'
TIMEZONE = 'America/New_York'
REVERSE_CATEGORY_ORDER = True
AVATAR = 'theme/images/me400x400.png'#{photo}admin-ajax.php_400x400.png'
DEFAULT_LANG = 'en'

# Paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

# Top menus
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# LOAD_CONTENT_CACHE = False
# Blogroll
# LINKS = (('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/GrilledChickenThighs'),
          ('Linkedin', 'https://www.linkedin.com/in/paul-mendes'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# MARKUP = ('md', 'ipynb')

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
PLUGIN_PATHS = ['./pelican-plugins','./plugins']
#What a headache https://github.com/getpelican/pelican-themes/issues/460
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
     'tipue_search',
    # 'liquid_tags.youtube',
    # 'liquid_tags.notebook',
    # 'liquid_tags.include_code',
    'render_math',
    'ipynb.markup']
I18N_TEMPLATES_LANG = 'en'

# LIQUID_CONFIGS = (('PATH', '.', "The default path"), ('SITENAME', 'Default Sitename', 'The name of the site'), ('FOO', 'Default for foo', 'A nonsense test'))

# for Tique Search Plugin
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')



CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

STATIC_PATHS = [ 'extra' ]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}
