
# coding:gbk
import urllib2
import re
import threading
import time
import os
def download(i):
    global num
    url='http://jandan.net/ooxx/page-%d#comments' %i
    urls=[]
    req=urllib2.urlopen(url).read()
    txt=re.compile(r'</a><br /><img src="//(.*?\.jpg)')
    result=txt.findall(req)
    for ii in result:
        urls.append(ii)
    for i in urls:
        t='http://'+i
        pic=urllib2.urlopen(t, timeout=10)
        p=re.findall(r'[A-z0-9]+\.jpg',i)
        p=''.join(p)
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        string='%s/%s' %(path,p)
        with open(string,'wb') as f:
            f.write(pic.read())
            print '%s�������\n' %p,
            num+=1

start=input('��������ʼҳ��')
end=input('��������ֹҳ��')
path=raw_input('���������ص�ַ:')
print '��ʼ����'
if __name__=='__main__':
    for i in range(start,end+1):
        t=threading.Thread(target=download,args=(i,))
        t.start()
        threads.append(t)
        t.join()
print 'һ��������%d��ͼƬ' %num
raw_input("please input ENTER to exit")
