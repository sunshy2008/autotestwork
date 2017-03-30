__author__ = 'Administrator'
import re
import urllib.request
response = urllib.request.urlopen('http://python.org/')
html = response.read()
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = getHtml("https://www.baidu.com/")

print(html)