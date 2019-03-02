#!/usr/bin/python3
#! _*_ coding:utf-8 _*_

'''
爬取市场营销栏目的论文
'''

import re 
import requests
import time
import json
from requests.exceptions import RequestException

#get_one_page()函数用于获取要获取的url网页内容
def get_one_page(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        return response.text
    return None

#parse_one_page()函数中传入要解析的网页内容
def parse_one_page(html):
    #生成正则对象
    pattern = re.compile('<li><span>(.*?)</span><a href="(.*?)".*?>(.*?)</a>',re.S)
    item = re.findall(pattern,html)
    for i in item:
        yield{
            '时间':i[0],
            '网址':i[1],
            '标题':i[2]
        }

def write_to_file(content):
    with open ('论文2.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
    
def main(addr):
    url='http://www.lunwendata.com/61_{page}.html'.format(page = addr)
    print(url)
    html = get_one_page(url)
    for r in parse_one_page(html):
        write_to_file(r)

if __name__ == '__main__':
    for r in range(30):
        main(addr = r)
        time.sleep(1)
