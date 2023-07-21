# Scrapy settings for scrapy_yami project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_yami"

SPIDER_MODULES = ["scrapy_yami.spiders"]
NEWSPIDER_MODULE = "scrapy_yami.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapy_yami (+http://www.yourdomain.com)"

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
#     'cookie': 'bm_decision=undefined; bm_decision=undefined; 3rd_Party_Pixel=cpc; 3rd_Party_Pixel_utm_campaign=General_Industry_CH; 3rd_Party_Pixel_utm_source=google; YMB_TK=eyJhdXRoIjoiOTI0YjRiOWZiN2YzZmMzNjhlNWZjYTQ1NjRiNTU2NzUiLCJkYXRhIjoiNDY1OTNhZDQtMzQ2Yy00MTY0LTk3NjEtOGJiMDYyMGJmOTZiIiwibm9uY2UiOiI1ODcxIiwidCI6MiwidHMiOjE2Nzg1MDQzNjUsInYiOjF9; YMB_LANG=zh_CN; _gcl_aw=GCL.1678504367.Cj0KCQiAx6ugBhCcARIsAGNmMbint2KtLSedtJ5EaTgeMK1LkFfbVlD5_ZkLfXs9OIVklihqOyzU1HkaAjWuEALw_wcB; _gcl_au=1.1.512656460.1678504367; optimizelyEndUserId=oeu1678504367157r0.9050377656010475; _gid=GA1.2.2093137965.1678504368; _gac_UA-39051355-1=1.1678504368.Cj0KCQiAx6ugBhCcARIsAGNmMbint2KtLSedtJ5EaTgeMK1LkFfbVlD5_ZkLfXs9OIVklihqOyzU1HkaAjWuEALw_wcB; _tt_enable_cookie=1; _ttp=QCLvVi_cMkb2kip4zYALc1_ZbOO; APPLE_PAY_AVALID=0; YMB_SHIELD_ID=759a1f0eca3449ef81f76cc35da7b98e; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22186cea81935f3-0b5d762569315a-26031851-2764800-186cea819362d3%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_utm_source%22%3A%22google%22%2C%22%24latest_utm_medium%22%3A%22cpc%22%2C%22%24latest_utm_campaign%22%3A%22general_industry%22%7D%2C%22%24device_id%22%3A%22186cea81935f3-0b5d762569315a-26031851-2764800-186cea819362d3%22%7D; ymb_track_visitor_id=b01219b3-3cac-8250-c3f5-50960e901234; ymb_track_session_id=a864800f-5db5-62e0-b32a-2e49697fe3a3; IR_gbd=yamibuy.com; CS_FPC=CSC8yK1j0s73MAmRK2dfjnpuP7GLhqF8j8M; CS_CTIME=1678504370580; _fbp=fb.1.1678504371019.2068847468; bm_decision=undefined; location_id=001; cookiepolicybar=0; zipcode=91702; IR_9694=1678504460320%7C0%7C1678504460320%7C%7C; _uetsid=9ade1b60bfba11eda4c92dcd33e498af; _uetvid=9ade51b0bfba11ed965dc1464d845e45; _ga_PWL198180G=GS1.1.1678504368.1.1.1678504461.31.0.0; cto_bundle=KvI2g19QVE9wbnI1QTdpNTNlME5BUDdmWG9ZTHY3SGFaRklUSllnbEN6S04wJTJGYllzd1ZoV0NqdWZET2JVaFpYZ0Y3JTJCcHBCMkdlV0p3ZDluV0ElMkZybE5vMDNiZGFhNG0lMkZRT2VMWXVBOFNNTjh2NG9DQm90MXppdklHeWNWTW5YdkdGWTIwSlM5a0k4bENrM3M5VkZBNVYlMkJWb3l3JTNEJTNE; _gat_gtag_UA_39051355_1=1; _ga_JN08G8MDMP=GS1.1.1678504373.1.1.1678504462.0.0.0; _ga=GA1.1.567560630.1678504368',
#     'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'none',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
#     }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapy_yami.middlewares.ScrapyYamiSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scrapy_yami.middlewares.ScrapyYamiDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "scrapy_yami.pipelines.ScrapyYamiPipeline": 300,
   "scrapy_yami.pipelines.ImagePiepeline": 299,
 
}

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
