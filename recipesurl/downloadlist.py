__author__ = '0neSe7en'
import urllib2
import re
from datetime import datetime
import gzip
from lxml import etree
from StringIO import StringIO
import pymongo
from bson import ObjectId


NAMESPACES = {'ns': "http://www.sitemaps.org/schemas/sitemap/0.9"}
RECIPE_GZ_PATTERN = re.compile(ur"recipe_\d*.xml.gz", re.MULTILINE)
RECIPE_URL_PATTERN = re.compile(ur"recipe/(\d+)", re.MULTILINE)
DTFMT = "%Y-%m-%d"

def get_urls(url):
    xml = urllib2.urlopen(url)
    recipe_xml_gz = gzip.GzipFile(fileobj=StringIO(xml.read()))
    recipe_xml = recipe_xml_gz.read()
    try:
        with open("recipes_url_list.txt", "a") as f:
            f.writelines("\n".join(re.findall(RECIPE_URL_PATTERN, recipe_xml)))
    except:
        return False
    return True

def download_list(lastmod=None):
    sitemap = urllib2.urlopen("http://www.xiachufang.com/sitemap.xml")
    sitemap_text = sitemap.read()
    recipes_xml = etree.fromstring(sitemap_text)
    sitemaps = recipes_xml.xpath("//ns:sitemap", namespaces=NAMESPACES)
    for sitemap in sitemaps:
        if re.search(RECIPE_GZ_PATTERN, sitemap[0].text):
            lastmod_dt = datetime.strptime(sitemap[1].text, "%Y-%m-%d")
            if (not lastmod) or (lastmod<lastmod_dt):
                if not get_urls(sitemap[0].text):
                    return False
    return True

def update_list(lastmod=None):
    conn = pymongo.Connection()
    db = conn.xiachufang
    collection = db.recipe
    recipe_id_list = download_list(lastmod=lastmod)
    for recipe_id in recipe_id_list:
        # if collection.

if __name__ == '__main__':
    print download_list()