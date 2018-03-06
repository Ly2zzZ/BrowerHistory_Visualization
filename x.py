# -*- coding:utf-8 -*-
import urllib2
import cookielib
from bs4 import BeautifulSoup
import sys 
reload(sys)
sys.setdefaultencoding('utf-8') 

def _get_new_data(page_url, soup):
    res_data = {}
    res_data['url'] = page_url
    res_data['description'] = soup.get_text(strip=True)
    return res_data


if __name__=='__main__':
    hdr = {'User-Agent':'Mozilla/5.0'}
    root_url = 'https://github.com/d3/d3-shape/blob/master/README.md#areas'
    req = urllib2.Request(root_url,headers=hdr)
    response = urllib2.urlopen(req)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'lxml', from_encoding='utf-8')
    data = _get_new_data(root_url, soup)

    x = open('asd.txt', 'w')
    x.writelines(str(data['description']))
