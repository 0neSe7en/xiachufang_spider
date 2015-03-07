# -*- coding: utf-8 -*-


BOT_NAME = 'xiachufang'
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'xiachufang.customdownloadermw.randomuseragent.RandomUserAgentMW':400
}
SPIDER_MODULES = ['xiachufang.spiders']
NEWSPIDER_MODULE = 'xiachufang.spiders'
ITEM_PIPELINES = {'xiachufang.pipelines.XiachufangPipeline': 300}
DOWNLOAD_DELAY = 0.5
LOG_LEVEL = 'INFO'
# LOG_FILE = "xcf-spider.log"
COOKIES_ENABLED = False
RETRY_ENABLED = True
REDIRECT_ENABLED = False
CONCURRENT_REQUESTS = 3