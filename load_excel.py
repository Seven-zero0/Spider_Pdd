"""
@author:Administrator
@file:load_excel.py
@time:2020/05/09
"""
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
import xlrd


class OpenExcel(object):
    def __init__(self, book_name):
        self.book_name = book_name
        self.workbook = self.open_workbook()
        self.wb = load_workbook(filename=self.book_name)
        self.bg_color = PatternFill('solid', fgColor='92d050')  # 设置背景色

    def open_workbook(self):
        return xlrd.open_workbook(self.book_name)

    def get_book(self):
        table = self.workbook.sheets()[0]
        item = []
        for rown in range(table.nrows):
            array = {'编号': '', '名称': '', 'url': '', 'type': '', 'rown': ''}
            array['编号'] = table.cell_value(rown, 0)
            array['名称'] = table.cell_value(rown, 1)
            array['url'] = table.cell_value(rown, 3)
            array['type'] = table.cell_value(rown, 6)
            array['rown'] = rown
            item.append(array)

        return item

    def get_url(self, data):
        item = []
        for i in data:
            if i['url'] == '拼多多链接':
                continue
            if i['url'] == '':
                continue
            item.append(i)
        return item

    def clear_url(self, item):
        item_url = []
        for i in item:
            if i['type'] != '已发布':
                item_url.append(i)
        return item_url

    def modify_excel(self, rown):
        ws = self.wb['Sheet1']
        row = 'G{}'.format(rown+1)  # 构建url
        ws[row] = '已发布'
        ws[row].fill = self.bg_color
        self.wb.save(self.book_name)

    def run(self):
        # 1.打开文件
        # 2.获取表单
        data = self.get_book()
        # 3. 获取url
        item = self.get_url(data)
        # 4. 处理只留下未发布的url
        item_url = self.clear_url(item)
        return item_url


