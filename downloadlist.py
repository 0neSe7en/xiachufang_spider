__author__ = '0neSe7en'
import urllib2
import re
import gzip
from StringIO import StringIO
BASE_URL = "http://www.xiachufang.com/sitemap/"
sitemap = urllib2.urlopen("http://www.xiachufang.com/sitemap.xml")
sitemap_text = sitemap.read()
p = re.compile(ur"recipe_\d*.xml.gz", re.MULTILINE)
recipe_url_pattern = re.compile(ur"http://www.xiachufang.com/recipe/\d*/", re.MULTILINE)
recipe_xml_list = re.findall(p, sitemap_text)
for xml_name in recipe_xml_list:
    xml = urllib2.urlopen(BASE_URL+xml_name)
    recipe_xml_gz = gzip.GzipFile(fileobj=StringIO(xml.read()))
    recipe_xml = recipe_xml_gz.read()
    with open("recipes_url_list.txt", "a") as list_file:
        list_file.writelines([url+"\n" for url in re.findall(recipe_url_pattern, recipe_xml)])