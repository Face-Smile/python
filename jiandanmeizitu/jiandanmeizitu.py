# coding:gbk
import requests
import urllib2
import re
import threading
import time
import os
def download(i):
    global num
    url='http://jandan.net/ooxx/page-%d#comments' %i
    urls=[]
    print url
    headers={"Host":"jandan.net",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; W��) Gecko/20100101 Firefox/56.0",
"Accept":"text/html,application/xhtml+xm��plication/xml;q=0.9,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",	
"Accept-Encoding":"gzip, deflate",
"Cookie	":"__cfduid=d3cc76cfacc58f3f53dedaf1426fc68d11510458274",
"Connection":"keep-alive"}
    req=requests.get(url, headers=headers)
    req=req.text
    txt=re.compile(r'</a><br /><img src="//(.*?\.jpg)')
    result=txt.findall(req)
    for ii in result:
        urls.append(ii)
    for i in urls:
        t='http://'+i
        print t
        pic=requests.get(t, timeout=10)
        p=re.findall(r'[A-z0-9]+\.jpg',i)
        p=''.join(p)
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        string='%s/%s' %(path,p)
        with open(string,'wb') as f:
            f.write(pic.content)
            print p+u'�������'
            num+=1

start=input('��������ʼҳ��')
end=input('��������ֹҳ��')
path=raw_input('���������ر����ַ:')
print '��ʼ����'
if __name__=='__main__':
    num=0
    threads=[]
    for i in range(start,end+1):
        t=threading.Thread(target=download,args=(i,))
        t.start()
        threads.append(t)
        t.join()
print 'һ��������%d��ͼƬ' %num

