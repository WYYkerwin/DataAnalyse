import re
import numpy
import string
import csv
import pandas as pd
import xlwt
from xlutils.copy import copy
import xlrd
import os
import codecs

f = codecs.open('DataRecord.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
line = f.readline()  # 以行的形式进行读取文件
# ROI = []
# SystemTime = []
# TimeStamp = []
# Pos = []
# LeftEye = []
# RightEye = []
DA = []
while line:
    a = line.split('  ')
    # b = a[0:1]  # 这是选取需要读取的位数
    # c = a[1:2]
    # d = a[2:3]
    # e = a[3:4]
    # F = a[4:5]
    # g = a[5:6]
    # b1 = ''.join(b)
    # c1 = ''.join(c)
    # d1 = ''.join(d)
    # e1 = ''.join(e)
    # F1 = ''.join(F)
    # g1 = ''.join(g)
    # g2 = g1.replace('\r\n','')
    # g3 = [''.join(g2)]
    # a1 = ''.join(a)
    # a2 = a1.replace('\r\n','')
    # a3 = [''.join(g2)]
    a1 = [x.strip() for x in a]
    DA.append(a1)
    # ROI.append(b)  # 将其添加在列表之中
    # SystemTime.append(c)
    # TimeStamp.append(d)
    # Pos.append(e)
    # LeftEye.append(F)
    # RightEye.append(g3)
    line = f.readline()
f.close()

name=['ROI','SystemTime','Timestamp','Pos','Left','Right']
test=pd.DataFrame(columns=name,data=DA)#数据有三列，列名分别为one,two,three
print(test)
test.to_csv('D:\清华实验\DataAnalyse/DataRecord.csv',encoding='gbk')























# for i in list1:
#     print(i)



# f = codecs.open('DataRecord.txt', "r", encoding='utf-8')
# lines = f.readline()  # 读取全部内容
# #print(lines)
# while lines:
#      a = lines.split()
# print(a)



# Light_time_1 = []
# Light_time_2 = []
# Light_time_3 = []
# Light_time_4 = []
# Barrier_time_1 = []
# Barrier_time_2 = []
# Barrier_time_3 = []
# Barrier_time_4 = []
# #print(lines)
#
#
# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         # print(root) #当前目录路径
#         # print(dirs) #当前路径下所有子目录
#         # print(files) #当前路径下所有非目录子文件
#         for file in files:
#             if os.path.splitext(file)[1] == '.txt':
#                 if 'Part'in os.path.split(file)[1]:
#                     print(os.path.join(root,file))
#                     Current_Path = os.path.join(root,file)
#
#
#                     f = open(Current_Path, "r", encoding='utf-8')
#                     lines = f.readlines()  # 读取全部内容
#                     Light_5 = []
#                     Barrier_5 = []
#                     for i in range(1, lines.__len__(), 1):  # (开始/左边界, 结束/右边界, 步长)
#
#                         list = []  ## 空列表, 将第i行数据存入list中
#                         for word in lines[i].split():
#                             word = word.strip(string.whitespace)
#                             list.append(word);
#                             #print(word)
#                         #print(list)
#
#                         # print(list[2])
#
#                         # 取出带L和B的元素
#                         Light = []
#                         for each in list:
#                             if 'L' in each:
#                                 Light.extend(list[list.index(each):list.index(each) + 2])
#                         #print(Light)
#
#                         Barrier = []
#                         for each in list:
#                             if 'B' in each:
#                                 # print(list.index(each))
#                                 Barrier.extend(list[list.index(each):list.index(each) + 2])
#                         #print(Barrier)
#
#                         Light_1 = []
#                         Barrier_1 = []
#
#                         Light_1.extend(Light[0:2])
#                         Barrier_1.extend(Barrier[0:2])
#
#                         # print(Barrier_1)
#                         #print(Light_1)
#
#                         # 筛除后缀为0的元素
#                         Light_2 = []
#                         Barrier_2 = []
#
#                         for each in Barrier_1:
#                             a = Barrier_1[1]
#                             if a == '1':
#                                 Barrier_2.append(each)
#                         # print(Barrier_2)
#
#                         for each in Light_1:
#                             b = Light_1[1]
#                             if b == '1':
#                                 Light_2.append(each)
#                         #print(Light_2)
#
#                         # 提取反应时数据
#                         Light_3 = []
#                         Barrier_3 = []
#
#                         for each in Barrier_2:
#                             if 'B' in each:
#                                 # print(list.index(each))
#                                 Barrier_3.append(each)
#                         # print(Barrier_3)
#
#                         for each in Light_2:
#                             if 'L' in each:
#                                 Light_3.append(each)
#                         #print(Light_3)
#
#                         # 利用正则表达式把反应时数值提取出来
#                         Barrier_4 = []
#                         Light_4 = []
#
#                         for each in Barrier_3:
#                             each = str(each)
#                             # float(re.findall(r"\d+\.?\d*", each))
#                             # print(re.findall(r"\d+\.?\d*", each))
#                             Barrier_4.append(re.findall(r"\d+\.?\d*", each))
#                         # print(Barrier_4)
#
#                         for each in Light_3:
#                             each = str(each)
#                             # print(re.findall(r"\d+\.?\d*", each))
#                             Light_4.append(re.findall(r"\d+\.?\d*", each))
#                         #print(Light_4)
#
#                         # 将所有反应时合并为一个list
#
#                         for each in Barrier_4:
#                             for a in each:
#                                 a = float(a)
#                                 Barrier_5.append(a)
#
#                         for each in Light_4:
#                             for b in each:
#                                 b = float(b)
#                                 Light_5.append(b)
#                     #print(Light_5)
#                     #print(Barrier_5)
#
#                     # 求均值
#                     #print(numpy.mean(Light_5))
#                     #print(numpy.mean(Barrier_5))
#                     # print(list[2])
#
#                     # 生成barrier+方位结果的数列
#                     if list[2] == '1':
#                         Barrier_time_1.append(numpy.mean(Barrier_5))
#                     elif list[2] == '2':
#                         Barrier_time_2.append(numpy.mean(Barrier_5))
#                     elif list[2] == '3':
#                         Barrier_time_3.append(numpy.mean(Barrier_5))
#                     elif list[2] == '4':
#                         Barrier_time_4.append(numpy.mean(Barrier_5))
#
#                     #print(Barrier_time_1)
#                     #print(Barrier_time_2)
#                     #print(Barrier_time_3)
#                     #print(Barrier_time_4)
#
#                     if list[2] == '1':
#                         Light_time_1.append(numpy.mean(Light_5))
#                     elif list[2] == '2':
#                         Light_time_2.append(numpy.mean(Light_5))
#                     elif list[2] == '3':
#                         Light_time_3.append(numpy.mean(Light_5))
#                     elif list[2] == '4':
#                         Light_time_4.append(numpy.mean(Light_5))
#
#                     #print(Light_time_1,Light_time_2,Light_time_3,Light_time_4)
#
#
#
#
# file_name(r'C:\Users\86186\Desktop\drive\drive')
#
# #numpy.array(Barrier_time_1)
# #numpy.array(Barrier_time_2)
# Barrier_time = []
# Barrier_time.append(Barrier_time_1)
# Barrier_time.append(Barrier_time_2)
# Barrier_time.append(Barrier_time_3)
# Barrier_time.append(Barrier_time_4)
# #print(Barrier_time)
# Light_time = []
# Light_time .append(Light_time_1)
# Light_time .append(Light_time_2)
# Light_time .append(Light_time_3)
# Light_time .append(Light_time_4)
# print(Barrier_time)
# print(Light_time)
# """
# print(Barrier_time_3)
# print(Barrier_time_4)
# print(Light_time_1)
# print(Light_time_2)
# print(Light_time_3)
# print(Light_time_4)
# print(len(Light_time_4))
#
# """
#
# def write_excel_xls(path, sheet_name, value):
#     index = len(value)  # 获取需要写入数据的行数
#     workbook = xlwt.Workbook()  # 新建一个工作簿
#     sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
#     for i in range(0, index):
#         for j in range(0, len(value[i])):
#             sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
#     workbook.save(path)  # 保存工作簿
#     print("xls格式表格写入数据成功！")
#
# book_name_xls = '实验数据.xls'
# sheet_name_xls = '实验数据'
# value_title = [["1", "2", "3", "4", "5","6","7","8","9","10", "11", "12", "13", "14","15","16","17","18","19", "20", "21", "22","23","24", "25", "26", "27", "28","29","30"], ]
# write_excel_xls(book_name_xls, sheet_name_xls, value_title)
#
# def write_excel_xls_append(path, value):
#     index = len(value)  # 获取需要写入数据的行数
#     workbook = xlrd.open_workbook(path)  # 打开工作簿
#     sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
#     worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
#     rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
#     new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
#     new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
#     for i in range(0, index):
#         for j in range(0, len(value[i])):
#             new_worksheet.write(i+rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
#         new_workbook.save(path)  # 保存工作簿
#     print("xls格式表格【追加】写入数据成功！")
#
# write_excel_xls_append(book_name_xls, Barrier_time)
# write_excel_xls_append(book_name_xls, Light_time)
