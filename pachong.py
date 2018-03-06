#coding:utf-8
import socket
import json
import cookielib
import socket
import urllib2
from bs4 import BeautifulSoup
import sys 
reload(sys)
sys.setdefaultencoding('utf-8') 

def _get_new_data(page_url, soup):
    res_data = {}
    res_data['url'] = page_url
    res_data['description'] = soup.find(attrs={"name": "description"})['content']
    res_data['keywords'] = soup.find(attrs={"name": "keywords"})['content']
    return res_data




if __name__=='__main__':
    hdr = {'User-Agent':'Mozilla/5.0'}
    socket.setdefaulttimeout(1.0)
    x = open('blogCblog.txt','w')

    f=open('history.json','r')
    r= f.read()
    r=r.decode("utf-8-sig")
    c=json.loads(r)

    Scount = 0;
    Ecount = 0; 
    for line in c:
        root_url=line['url']
        if "http" in root_url:
            print(root_url)
            try:
                req = urllib2.Request(root_url,headers=hdr)
                response = urllib2.urlopen(req)
                html_content = response.read()
                soup = BeautifulSoup(html_content, 'lxml', from_encoding='utf-8')
                data = _get_new_data(root_url, soup)
                x.writelines(str(data['description']))
                x.writelines(str(data['keywords']))
                Scount+=1
                print ("Succed!  SuccedNum:%d ErrorNum:%d"%(Scount,Ecount))
            except:
                x.writelines(line['title'])
                Scount+=1
                print ("Succed!  SuccedNum:%d ErrorNum:%d"%(Scount,Ecount))
            else:
                Ecount+=1
                print ("Succed!  SuccedNum:%d ErrorNum:%d"%(Scount,Ecount))





    
    

