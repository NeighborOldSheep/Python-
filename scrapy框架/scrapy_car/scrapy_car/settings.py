# Scrapy settings for scrapy_car project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_car"

SPIDER_MODULES = ["scrapy_car.spiders"]
NEWSPIDER_MODULE = "scrapy_car.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapy_car (+http://www.yourdomain.com)"

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)  
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': 'ASP.NET_SessionId=tlusk5yfk3vt1qmkdzvyghx3; fvlid=1678479664855zHnLFwKxFP; sessionip=68.119.146.182; sessionid=31374E6D-7A5B-47DB-A61D-AF0C3695272D%7C%7C2023-03-11+04%3A21%3A08.922%7C%7Cwww.google.com; autoid=c4ecda9e8f74913f3a2deafb61b68606; area=999999; sessionuid=31374E6D-7A5B-47DB-A61D-AF0C3695272D%7C%7C2023-03-11+04%3A21%3A08.922%7C%7Cwww.google.com; __ah_uuid_ng=c_31374E6D-7A5B-47DB-A61D-AF0C3695272D; sessionfid=2087611463; jrsfvi=1678479744590eNdjq8EzUx%7Cwww.autohome.com.cn%7C6829651; jrslvi=6829651%7Cwww.autohome.com.cn%7C1678479744590eNdjq8EzUx; orderCount=eyJzaXRlSWQiOiI1MSIsImNhdGVnb3J5SWQiOiI4MjEiLCJzdWJDYXRlZ29yeUlkIjoiMTU0MjAiLCJ1c2VySWQiOiIiLCJwdmlkQ2hhaW4iOiIzMzExNjY3LDY4Mjk2NTEiLCJhY2Nlc3NUeXBlIjoiMSIsImFwcEtleSI6IiIsImxvY0NpdHlJZCI6IjExMDEwMCIsImxvY1Byb3ZpbmNlSWQiOiIxMTAwMDAiLCJkZXZpY2VJZCI6IiIsImxvYWRJZCI6IjE2Nzg0Nzk3NDQ1OTBlTmRqcThFelV4Iiwic2Vzc2lvbklkIjoiMzEzNzRFNkQtN0E1Qi00N0RCLUE2MUQtQUYwQzM2OTUyNzJEfHwyMDIzLTAzLTExKzA0OjIxOjA4LjkyMnx8d3d3Lmdvb2dsZS5jb20iLCJ2aXNpdF9pbmZvIjoiMzEzNzRFNkQtN0E1Qi00N0RCLUE2MUQtQUYwQzM2OTUyNzJEfHwyMzUwQTI4My1BRkM2LTQyMEEtQjRDMi04NDc4NzZBNTM5Nzh8fDIwMjAwNTA5fHwwMXx8MyIsImN1clB2YXJlYUlkIjoiNjgyOTY1MSIsInB2YXJlYUlkIjoiIn0=; sessionvid=D49E31B9-02A5-495B-8B11-789FAE19744D; pvidlist="030d85d5-b2f2-406e-8049-d6d9b2ef8d335:551166:860984:0:1:4408549,80597068-83e9-488d-b792-efb0d1410d613:550947:860664:0:1:4408273"; ahsids=4658; ahpvno=10; pvidchain=3311273,3454439; v_no=5; visit_info_ad=31374E6D-7A5B-47DB-A61D-AF0C3695272D||D49E31B9-02A5-495B-8B11-789FAE19744D||-1||-1||5; ref=www.google.com%7C0%7C0%7C0%7C2023-03-11+05%3A10%3A05.869%7C2023-03-11+04%3A21%3A08.922; ahrlid=1678482601565AJG2bJRKL0-1678482618494',
    'Referer': 'https://car.autohome.com.cn/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapy_car.middlewares.ScrapyCarSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scrapy_car.middlewares.ScrapyCarDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapy_car.pipelines.ScrapyCarPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
