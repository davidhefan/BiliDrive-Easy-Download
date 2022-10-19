#!/usr/bin/python
# coding=utf-8

import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple

def getColumnIndex(table, columnName):
    columnIndex = None
    #print table
    for i in range(table.ncols):
        #print columnName
        #print table.cell_value(0, i)
        if(table.cell_value(0, i) == columnName):
            columnIndex = i
            break
    print(columnName, columnIndex)
    return columnIndex

def readExcelDataByName(fileName, sheetName):
    #print fileName
    data = xlrd.open_workbook(fileName)
    table = data.sheet_by_name(sheetName)
    print(table.ncols, table.nrows)
    return table

def readExcelDataByIndex(fileName, sheetIndex):
    data = xlrd.open_workbook(fileName)
    table = data.sheet_by_index(sheetIndex)
    return table

def get_cell_value(table, row_indx, col_indx):
    if col_indx is not None:
        ctype = table.cell(row_indx, col_indx).ctype
        cell = table.cell_value(row_indx, col_indx)
        if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
            cell = int(cell)  # 浮点转成整型
            cell = str(cell)  # 转成整型后再转成字符串，如果想要整型就去掉该行
        elif ctype == 3:
            date = datetime(*xldate_as_tuple(cell, 0))
            cell = date.strftime('%Y/%m/%d %H:%M:%S')
        elif ctype == 4:
            cell = True if cell == 1 else False
        return cell
    return ''

# if __name__ == '__main__':
#     max_num = 10
#
#     #example
#     xlsfile= '/Users/davidhe/Downloads/test/stu_result.xlsx'
#
#     excel_table = readExcelDataByName(xlsfile, '不存在')
#
#     stu_number_index = getColumnIndex(excel_table, '考号')
#     stu_name_index = getColumnIndex(excel_table, '姓名')
#     stu_school_index = getColumnIndex(excel_table, '学校')
#     stu_class_index = getColumnIndex(excel_table, '班级')
#     stu_img_path_index = getColumnIndex(excel_table, '图片地址')
#     stu_score_index = getColumnIndex(excel_table, '分数')
#
#     for i in range(1, excel_table.nrows):  # 取长度
#         stu_number = get_cell_value(excel_table, i, stu_number_index)
#         stu_name = get_cell_value(excel_table, i, stu_name_index)
#         stu_school = get_cell_value(excel_table, i, stu_school_index)
#         stu_class = get_cell_value(excel_table, i, stu_class_index)
#         stu_img_path = get_cell_value(excel_table, i, stu_img_path_index)
#         stu_score = get_cell_value(excel_table, i, stu_score_index)
#
#         print(i, stu_number, stu_name, stu_school, stu_class, stu_img_path, stu_score)
#
#         if i == max_num:
#             break