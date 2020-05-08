"""
@author:Administrator
@file:main.py
@time:2020/05/07
"""

import requests
import re
from bs4 import BeautifulSoup
import json
import time
import random
import os

from urllib.request import urlretrieve


class SpiderPdd(object):
    def __init__(self, url_start):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Ch'
                          'rome/81.0.4044.122 Safari/537.36'}
        self.url = url_start
        self.num = 0
        self.path = r'C:\Users\Zero\Documents\leidian\Pictures'

    def get_url(self):
        res = requests.get(self.url, headers=self.headers)
        res = res.content.decode('utf-8')
        with open('ceshi3.html', 'w', encoding='utf-8') as f:
            f.write(res)
        return res

    def open_html(self):
        with open('ceshi.html', 'r', encoding='utf-8') as f:
             html_data = f.read()
        return html_data

    def get_data(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        try:
            soup1 = soup.find_all('script')[4]
        except Exception as e:
            try:
                soup1 = soup.find_all('script')[3]
            except Exception as e:
                soup1 = soup.find_all('script')[5]

        soup2 = soup1.get_text()
        pattern = r'window.rawData=\s{(.*?)};\n'
        result = re.findall(pattern, soup2)[0]
        result_data = '{'+result+'}'
        return result_data

    def get_result(self, result):
        result = json.loads(result)
        end_data = result['store']['initDataObj']['goods']['viewImageData']
        images_item = []
        for i in end_data:
            images_item.append(i)

        images = result['store']['initDataObj']['goods']['detailGallery']
        for image in images:
            images_item.append(image['url'])
        name = result['store']['initDataObj']['goods']['goodsName']   # 名称
        # 创建文件夹
        try:
            os.mkdir(self.path+'./{}'.format(name))
        except FileExistsError as e:
            pass

        # context = result['store']['initDataObj']['goods']['goodsID']    # 宝贝id
        return images_item, name

    def down_image(self, urls, name):
        """图片下载"""
        for url in urls:
            self.num += 1
            time.sleep(random.randint(0, 1))
            urlretrieve(url, self.path+'/{}/'.format(name)+name+'{}.jpg'.format(self.num))

    def run(self):
        html_data = self.get_url()
        # html_date = self.open_html()
        data = self.get_data(html_data)
        images_item, name = self.get_result(data)
        self.down_image(images_item, name)


if __name__ == '__main__':
    url = 'http://yangkeduo.com/goods.html?goods_id=801187988&refer_page_name=search_opt&refer_page_id=23699_1588920057214_hej6dsulv3&refer_page_sn=23699&_x_link_id=8a79d0ee-358d-4509-a7c5-b8d360d7f8a0&_x_goods_id=801187988'
    sp = SpiderPdd(url)
    sp.run()
