# encoding: utf-8
'''
@author: lingshu
@file: read_excel.py
@time: 2019/6/21 17:03
@desc: 读取excel
'''
import xlrd
from utils import get_file_path
def read_excel():
    file_path = get_file_path.get_root_path()+'testdata\\testdata.xlsx'
    # 文件位置
    excel_file=xlrd.open_workbook(file_path)

    # 获取sheet内容【1.根据sheet索引2.根据sheet名称】
    # sheet=ExcelFile.sheet_by_index(1)
    sheet = excel_file.sheet_by_name('Sheet1')
    # 打印sheet的名称，行数，列数
    print(sheet.name)
    print(sheet.nrows)
    print(sheet.ncols)

    # 获取整行或者整列的值
    rows = sheet.row_values(1)
    cols = sheet.col_values(1)
    print(rows)
    print(cols)

    #获取单元格内容
    print("第二行第一列的值为： %s",sheet.cell(1,0))

    # 打印单元格内容格式
    print("单元格内容格式为： %s",sheet.cell(0,0).ctype)

def get_xls():
    cls = []
    file_path = get_file_path.get_root_path() + 'testdata\\testdata.xlsx'
    # 文件位置
    excel_file = xlrd.open_workbook(file_path)
    sheet = excel_file.sheet_by_name('Sheet1')
    nrows = sheet.nrows
    for i in range(nrows):
        cls.append(sheet.row_values(i))
    return cls
if __name__ == '__main__':
    print(get_xls())