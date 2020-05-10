"""
@author:Administrator
@file:Spider.py
@time:2020/05/09
"""


import requests
import re
from bs4 import BeautifulSoup
import json
import time
import random
import os
from urllib.request import urlretrieve
from selenium import webdriver


class SpiderPdd(object):
    """爬虫部分"""

    def __init__(self):
        self.headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'yangkeduo.com',
        }
        self.proxies = self.random_ip
        self.num = 0

    @property
    def random_ip(self):
        with open('ip.json', 'r', encoding='utf-8') as f:
            data = f.read()

        data = json.loads(data)
        ip_lists = data['data']
        ip_list = []
        for i in ip_lists:
            array = {'http': ''}
            array['http'] = 'http://{}:{}'.format(i['ip'], i['port'])
            ip_list.append(array)

        return random.choice(ip_list)

    @property
    def user_agents(self):
        with open('UserAgent.txt', 'r', encoding='utf-8') as f:
            user_agents = f.read().splitlines()
        return user_agents

    def get_url(self, url, cookie):
        print('spider: requests方式')
        print(self.headers)
        print(self.proxies)
        cookies = {
            'cookie': '{}'.format(cookie)
        }
        res = requests.get(url, headers=self.headers, cookies=cookies)
        print('spider: 访问url1-2')
        print(cookies)
        time.sleep(3)
        res = res.content.decode('utf-8')
        time.sleep(3)
        print('spider: 访问url2')
        with open('ceshi4.html', 'w', encoding='utf-8') as f:
            f.write(res)
        return res

    def open_html(self):
        with open('ceshi.html', 'r', encoding='utf-8') as f:
            html_data = f.read()
        return html_data

    def get_data(self, data):
        print('spider:获取数据1')
        soup = BeautifulSoup(data, 'html.parser')
        try:
            print('spider:获取数据2')
            soup1 = soup.find_all('script')[5]
        except Exception as e:
            print(e)

        soup2 = soup1.get_text()
        print(soup2)
        pattern = r'window.rawData=\s{(.*?)};\n'
        result = re.findall(pattern, soup2)[0]
        result_data = '{' + result + '}'
        print('spider:获取数据4')
        return result_data

    def get_result(self, result, path_image):
        print('spider: 创建文件夹1')
        result = json.loads(result)
        print('spider: 创建文件夹2')
        end_data = result['store']['initDataObj']['goods']['viewImageData']
        print('spider: 创建文件夹3')
        images_item = []
        print('spider: 创建文件夹4')
        for i in end_data:
            images_item.append(i)

        images = result['store']['initDataObj']['goods']['detailGallery']
        print('spider: 创建文件夹5')
        for image in images:
            images_item.append(image['url'])
        name = result['store']['initDataObj']['goods']['goodsName']  # 名称
        # 对名字进行过滤
        char_list = '[/*/|/:/?///</>/"/\\/ //,/;]'

        name = re.sub(char_list, '', name)
        # 创建文件夹
        try:
            print('spider: 创建文件夹4')
            os.mkdir(path_image + './{}'.format(name))
        except FileExistsError as e:
            pass
        except Exception as e:
            print('spider: 创建文件夹5')
            print(e)
            os.mkdir(path_image + '/{}'.format(name))

        # context = result['store']['initDataObj']['goods']['goodsID']    # 宝贝id
        return images_item, name

    def down_image(self, urls, name, path_image):
        """图片下载"""
        print('spider: 下载图片')
        for url in urls:
            self.num += 1
            print('spider:下载图片1~xxx')
            time.sleep(random.randint(0, 1))
            urlretrieve(url, path_image + '/{}/'.format(name) + name + '{}.jpg'.format(self.num))

        return 1

    def run(self, url, path_image, cookie):
        # 访问url
        try:
            """ 完全运行OK，抛出1，否则 0"""
            html_data = self.get_url(url, cookie)
            # u获取数据
            data = self.get_data(html_data)
            # 获取数据，创建文件夹
            images_item, name = self.get_result(data, path_image)
            # 保存
            result = self.down_image(images_item, name, path_image)
            return result
        except Exception as e:
            return 2


if __name__ == '__main__':
    url = input('请输入url连接：\n')
    path_image = r'C:\Users\Administrator\Desktop\image'
    cookie = ''
    sp = SpiderPdd()
    sp.run(url, path_image, cookie)
