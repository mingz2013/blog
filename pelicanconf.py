#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# 基本配置

AUTHOR = u'Mingz'  # 默认作者

USE_FOLDER_AS_CATEGORY = True  # 用目录作为类别
DEFAULT_CATEGORY = 'misc'  # 默认文章分类

# DISPLAY_PAGES_ON_MENU = True  # 是否在模板菜单上显示页面
# DISPLAY_CATEGORIES_ON_MENU = True  # 是否在模板菜单上显示分类
DEFAULT_DATE = "fs"  # (2012, 3, 2, 14, 1, 1) 默认日期
# global metadata to all the contents
DEFAULT_METADATA = {
    'status': 'draft',
}  # 文章和页面的默认元数据设置
# FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2}).*'
DELETE_OUTPUT_DIRECTORY = False  # 删除putput目录，优点在于避免生成不必要的文件，同时， 该设置具有一定风险，请谨慎处理。
JINJA_EXTENSIONS = []  # 使用Jinja扩展列表
JINJA_FILTERS = {}  # Jinja2 filters自定义列表

OUTPUT_PATH = 'output'  # 文件生成目录
PATH = 'content'  # 输入文件目录
PAGE_PATHS = ['pages', ]  # 页面生成目录
ARTICLE_PATHS = ['articles', ]  # 文章输入文件目录
# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = False  # 定义是否使用文档相对URL链接，只有当测试时设置为 True

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'sitemap',
]  # 插件

SITEMAP = {
    'format': "xml",

}

SITENAME = u"Mingz's Blog"  # 站点名称
SITESUBTITLE = u"Mingz's blog on GitHub Page"
SITEURL = 'http://localhost/'  # 站点url,测试

TIMEZONE = 'Europe/Paris'

#TYPOGRIFY = True  # 如果设置为True, 一些排版效果将会纳入生成的HTML文件中，通过 Typogrify 库, 安装方式: pip install typogrify

# DIRECT_TEMPLATES = ('index', 'tags', 'categories',
#                     'archives')  # 直接使用模板。 通常情况下直接使用模板生成index页面的内容，(e.g., tags and category index pages). 如果无需标签和分类合集,设置 DIRECT_TEMPLATES = ('index', 'archives')
# PAGINATED_DIRECT_TEMPLATES = ('index',)  # 提供可以分页的模板
SUMMARY_MAX_LENGTH = 50  # 文章摘要最大字数。

# URL配置
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# 日期格式和语言环境
# DATE_FORMATS = {}  # 日期格式设置
DEFAULT_DATE_FORMAT = '%a %d %B %Y'  # 默认日期格式
LOCALE = "C"

# 模板页面
# custom page generated with a jinja2 template
# TEMPLATE_PAGES = {
#     # 'pages/jinja2_template.html': 'jinja2_template.html',
# } # 包含文章生成时的模板页

# 路径元数据
# static paths will be copied under the same name
# static paths will be copied without parsing their contents
STATIC_PATHS = [
    "images",
    "pdfs",
    # 'extra/robots.txt',
    # 'extra/CNAME',
    # 'extra/README.md'
]  # 在output目录中提供可访问的静态路径 “static”.
EXTRA_PATH_METADATA = {
    # 'extra/robots.txt': {'path': 'robots.txt'},
    # 'extra/CNAME': {'path': 'CNAME'},
    # 'extra/README.md': {'path': 'README.md'},
}

# Feed 设置
# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None
# FEED_ALL_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# 分页
# DEFAULT_ORPHANS
DEFAULT_PAGINATION = 10  # 分页长度
# PAGINATION_PATTERNS = (
#     (1, '{base_name}/', '{base_name}/index.html'),
#     (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
# )

# 云标签
# TAG_CLOUD_STEPS = 4
# TAG_CLOUD_MAX_ITEMS = 100

# 翻译
# 内容排序

# 主题
THEME = "themes/mycustomtheme"  # 主题
# THEME = 'notmyidea'
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
# CSS_FILE = 'main.css'
# * notmyidea
# * simple (a synonym for "plain text" :)


GITHUB_URL = 'http://github.com/mingz2013'
# DISQUS_SITENAME = "mingz's home"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True

DEFAULT_LANG = u'en'

# Blogroll
LINKS = (('mingz', 'http://mingz.me'),
         ('github', 'http://github.com/mingz2013'),
         ('csdn', 'http://blog.csdn.net/mingzznet'),
         # ('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (('github', 'http://github.com/mingz2013'),
          ('csdn', 'http://blog.csdn.net/mingzznet'),
          # ('twitter', 'http://twitter.com/ametaireau'),
          )

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
