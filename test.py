# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import sys
import io
from urllib.parse import quote
n=0
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
file_medicine = open('4.txt',mode='w',encoding='utf-8')
medicine_list=['头孢','板蓝根']
count=1
n=n+1
name=quote('头孢')
url = 'http://www.china-yao.com/?act=search&typeid=1&keyword='+name+'&page=' + str(n)
req = urllib.request.Request(url=url)
data = urllib.request.urlopen(req)
data = data.read()
dammit = UnicodeDammit(data, ["utf-8", 'gbk'])
data = dammit.unicode_markup
soup = BeautifulSoup(data, 'lxml')
tags = soup.select('tr td')
for tag in tags:
    if count%6!=0:
        file_medicine.write(tag.text+',')
    if count%6 == 0:
        file_medicine.write(tag.text+'\n')
    count+=1
print(count)
    #print(type(soup))
