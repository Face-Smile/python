# coding:gbk
import random
import string
t=[]
for i in range(0,200):
    a=list(string.ascii_letters)
    random.shuffle(a)
    ticket=''.join(a[:8])
    t.append(ticket)
    print ticket
st=set(t)
if len(t)==len(st):
    print '成功生成200个优惠券'
else:
    print '优惠券有重复'
