#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/11/21 16:11
# @Author  : Wilson
# @Version : 0.8

#导入库文件
import requests
from bs4 import BeautifulSoup
import time

# 网络请求的请求头
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'cookie': 'als=0; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1511251243; ctid=14; _ga=GA1.2.1591563536.1511251169; lps=http%3A%2F%2Fbeijing.anjuke.com%2Fsale%2Fp1%7C; sessid=F8C8D19B-F828-BE4C-E396-A30E803A81C6; aQQ_ajkguid=7A3F296F-FB53-4FA4-3019-B2397DA2D39B; twe=2; 58tj_uuid=5a897633-7256-4ad5-9b57-5217588dc44a; new_session=1; init_refer=; new_uv=5'
        }

#迭代页数
def get_more_page(start, end):
    for page in range(start, end):
        get_page(url + str(page))
        print("正在爬取第" + str(page) + "页...")
        time.sleep(2)

#构造爬取函数
def get_page(url,data=None):

    #获取URL的requests
    wb_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(wb_data.text,'lxml')

    #定义爬取的数据
    titles = soup.select('div.house-details > div.house-title > a')
    rooms = soup.select('div.house-details > div:nth-of-type(2) > span:nth-of-type(1)')
    meters = soup.select('div.house-details > div:nth-of-type(2) > span:nth-of-type(2)')
    floors = soup.select('div.house-details > div:nth-of-type(2) > span:nth-of-type(3)')
    years = soup.select('div.house-details > div:nth-of-type(2) > span:nth-of-type(4)')
    locations = soup.select('div.details-item > span.comm-address')
    costs = soup.select('div.pro-price > span.price-det > strong')
    # print(locations)

    #在获取到的数据提取有效内容
    if data==None:
        for title,room,meter,floor,year,location,cost in zip(titles,rooms,meters,floors,years,locations,costs):
            data = [
                title.get_text(),
                room.get_text(),
                meter.get_text(),
                floor.get_text(),
                year.get_text(),
                location.get_text(),
                cost.get_text()
            ]
            # print(data)
            saveFile(data)

#定义保存文件函数
def saveFile(data):
    path = "/Users/Wilson/Desktop/anjuke.txt"
    file = open(path,'a')
    file.write(str(data))
    file.write('\n')
    file.close()

#主体
#定义爬取页数
pages = 1 + int(input('请输入页码\n'))

#定义将要爬取的URL
url = 'https://beijing.anjuke.com/sale/p'

# #开始爬取
get_more_page(1,pages)
