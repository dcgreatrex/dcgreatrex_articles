#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David Greatrex'
SITENAME = 'dcgreatrex articles'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# This requires Pelican 3.3+
STATIC_PATHS = ['images', 'pages', 'favicon.png']

# Theme and plugins
THEME = 'pelican-octopress-theme/'
# PLUGIN_PATHS = ['pelican-plugins/']
# PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
#            'liquid_tags.include_code', 'liquid_tags.notebook',
#            'liquid_tags.literal']

#Github include settings
GITHUB_USER = 'dcgreatrex'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = False
GITHUB_SHOW_USER_LINK = False

# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'

# Search
SEARCH_BOX = True

NEWEST_FIRST_ARCHIVES = False

# Social media
FACEBOOK_LIKE = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
