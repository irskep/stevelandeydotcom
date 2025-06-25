AUTHOR = 'Steve Landey'
SITENAME = 'Steve Landey'
SITEURL = ""

PATH = "content"

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://linkedin.com/in/stevelandey"),
    ("GitHub", "https://github.com/irskep"),
    ("Email", "mailto:steve@stevelandey.com"),
)

DEFAULT_PAGINATION = False

# Theme configuration
THEME = 'theme'

# Markdown configuration
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.attr_list': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.md_in_html': {},
    },
    'output_format': 'html5',
}

# Static files
STATIC_PATHS = ['CNAME']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
