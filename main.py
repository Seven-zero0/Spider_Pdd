"""
@author:Administrator
@file:main.py
@time:2020/05/07
"""

import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import json


class SpiderPdd(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Ch'
                          'rome/81.0.4044.122 Safari/537.36'}
        self.url = 'http://yangkeduo.com/goods.html?goods_id=110978433004&refer_page_name=search_opt&refer_page_id=23699_1588867386044_ofww112kg3&refer_page_sn=23699&_x_link_id=53f48de9-ff6c-452f-9d18-ed3e68b82d8f&_x_goods_id=110019063290'

    def get_url(self):
        res = requests.get(self.url, headers=self.headers)
        res = res.content.decode('utf-8')
        with open('ceshi.html', 'w', encoding='utf-8') as f:
            f.write(res)

    def open_html(self):
        with open('ceshi.html', 'r', encoding='utf-8') as f:
             html_data = f.read()

        return html_data

    def get_data(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        soup1 = soup.find_all('script')[4]
        soup2 = soup1.get_text()
        pattern = r'window.rawData=\s{(.*?)};\n'
        result = re.findall(pattern, soup2)[0]
        result_data = '{'+result+'}'
        return result_data

    def get_result(self, result):
        result = json.loads(result)
        end_data = result['store']['initDataObj']['goods']['viewImageData']
        for i in end_data:
            print(i)
        images = result['store']['initDataObj']['goods']['detailGallery']
        for image in images:
            print(image)

    def run(self):
        # self.get_url()
        html_date = self.open_html()
        data = self.get_data(html_date)
        self.get_result(data)


if __name__ == '__main__':
    sp = SpiderPdd()
    sp.run()
