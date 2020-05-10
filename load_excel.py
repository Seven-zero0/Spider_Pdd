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
        # return openpyxl.load_workbook(self.book_name)
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
            # print(i['编号'])

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
        # print(item_url)
        return item_url

    def modify_excel(self, rown):
        print('excel正在修改')
        ws = self.wb['Sheet1']
        # for i in item_url:
        row = 'G{}'.format(rown+1)  # 构建url
        ws[row] = '已发布'
        ws[row].fill = self.bg_color

        self.wb.save('ceshi2.xlsx')
        print('excel保存完成')

    def run(self):
        # 1.打开文件
        # 2.获取表单
        print('3xxxxxx')
        data = self.get_book()
        print('4xxx')
        # 3. 获取url
        item = self.get_url(data)
        # return item
        # 4. 处理只留下未发布的url
        print('5xxx')
        item_url = self.clear_url(item)
        # # 5. 修改未发布的改为已发布
        # self.modify_excel(item_url)
        # for i in item:
        #     print(i)
        return item_url
        # print(item_url)

        # url_status = []
        # for i in item_url:
        #     url_item = {'编号': '', '名称': '', 'url': '', 'type': '', 'rown': '', 'status': ''}
        #     url = i['url']
        #     # status = self.start_spider(url=url, save_image_path=save_image_path, cookie=cookie)
        #     url_item['编号'] = i['编号']
        #     url_item['名称'] = i['名称']
        #     url_item['url'] = i['url']
        #     url_item['type'] = i['type']
        #     url_item['rown'] = i['rown']
        #     # url_item['status'] = status
        #     url_status.append(url_item)
        #     # print(url_item)
        # print(url_status)


if __name__ == '__main__':
    book_name = r'G:/job/python/Spider_Pdd/stores.xlsx'
    oe = OpenExcel(book_name)
    oe.run()
