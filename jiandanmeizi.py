# version:python2.7.13
# time:2017.08.01
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
        urls.append(ii)   #获取图片网址
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
            print '%s下载完成\n' %p, #下载图片
            num+=1
start=input('请输入起始页：')
end=input('请输入终止页：')
path=raw_input('请输入下载地址:')
print '开始下载'
num=0
threads=[]
if __name__=='__main__':
    for i in range(start,end+1):  #多线程创建
        t=threading.Thread(target=download,args=(i,))
        t.start()
        threads.append(t)
        t.join()
print '一共下载了%d张图片' %num
raw_input("please input ENTER to exit")
