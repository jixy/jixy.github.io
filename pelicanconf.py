#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'jixiangyang'
SITENAME = u'Laputa'
SITEURL = 'http://www.jixiangyang.com'

GITHUB_URL = 'https://github.com/jixy'
ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARCHIVE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

RELATIVE_URLS = True
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
THEME = 'pelican-themes/tuxlite_tbs'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_RSS = 'feeds/all/rss/xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['summary','sitemap']

## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('BYR', 'http://bbs.byr.cn'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/jixy'),
          (u'微博', 'http://weibo.com/u/1592567033'),)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
