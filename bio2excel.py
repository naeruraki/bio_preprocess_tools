"""
author:chimamo  https://github.com/CHIMAMO
date:2022-08-01
BIO生成excel文档
"""
import xlwt
import xlrd
from xlutils.copy import copy

global xls_file
xls_file = xlwt.Workbook(encoding='utf-8', style_compression=0)
f = open('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\LANN处理后BIO及BMES数据\\BIO20220808.txt', encoding='utf-8')
list_opr = []
list_ppt = []
list_emr = []
list_che = []
list_def = []
list_lbs = []
list_equ = []
list_gov = []
list_ust = []
list_edt = []
list_ins = []
list_tmp = []
list_str = []
list_ope = []
list_env = []
str_plus = ''
n = 0
for i in f:
    a = i.strip('\n').split('\t')
    if a == ['']:
        continue
    # print(a)
    if 'B-' in a[1]:
        list_tmp.append(a)
    if 'I-' in a[1]:
        list_tmp.append(a)
    if 'O' in a[1] and list_tmp != []:
        for k in list_tmp:
            str_plus += str(k[0])
            list_str.append(k[1])
        # print(list_tmp[0][1])
        if 'opr' in list_tmp[0][1]:
            list_opr.append(str_plus)
        if 'ppt' in list_tmp[0][1]:
            list_ppt.append(str_plus)
        if 'emr' in list_tmp[0][1]:
            list_emr.append(str_plus)
        if 'che' in list_tmp[0][1]:
            list_che.append(str_plus)
        if 'def' in list_tmp[0][1]:
            list_def.append(str_plus)
        if 'lbs' in list_tmp[0][1]:
            list_lbs.append(str_plus)
        if 'equ' in list_tmp[0][1]:
            list_equ.append(str_plus)
        if 'gov' in list_tmp[0][1]:
            list_gov.append(str_plus)
        if 'ust' in list_tmp[0][1]:
            list_ust.append(str_plus)
        if 'edt' in list_tmp[0][1]:
            list_edt.append(str_plus)
        if 'ins' in list_tmp[0][1]:
            list_ins.append(str_plus)
        if 'ope' in list_tmp[0][1]:
            list_ope.append(str_plus)
        if 'env' in list_tmp[0][1]:
            list_env.append(str_plus)
        list_tmp = []
        list_str = []
        str_plus = ''
def write_field_xls(path, sheet_name, value):
    index = len(value)
    # workbook = xlwt.Workbook()
    workbook = xls_file
    sheet = workbook.add_sheet(sheet_name)
    for i in range(0, index):
        sheet.write(i, 0, value[i])
    workbook.save(path)

def write_sheet_xls(path, sheet_name, value):
    index = len(value)
    rb = xlrd.open_workbook(path, formatting_info=True)
    workbook = copy(rb)
    sheet = workbook.add_sheet(sheet_name)
    for i in range(0, index):
        sheet.write(i, 0, value[i])
    workbook.save(path)

write_field_xls('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\高处坠落知识图谱数据\\中型标签分类.xls', 'opr', list_opr)
write_sheet_xls('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\高处坠落知识图谱数据\\中型标签分类.xls', 'ppt', list_ppt)
write_sheet_xls('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\高处坠落知识图谱数据\\中型标签分类.xls', 'emr', list_emr)
write_sheet_xls('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\高处坠落知识图谱数据\\中型标签分类.xls', 'che', list_che)
write_sheet_xls('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\高处坠落知识图谱数据\\中型标签分类.xls', 'def', list_def)
write_sheet_xls('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\高处坠落知识图谱数据\\中型标签分类.xls', 'lbs', list_lbs)
write_sheet_xls('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\高处坠落知识图谱数据\\中型标签分类.xls', 'equ', list_equ)
write_sheet_xls('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\高处坠落知识图谱数据\\中型标签分类.xls', 'gov', list_gov)
write_sheet_xls('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\高处坠落知识图谱数据\\中型标签分类.xls', 'ust', list_ust)
write_sheet_xls('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\高处坠落知识图谱数据\\中型标签分类.xls', 'edt', list_edt)
write_sheet_xls('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\高处坠落知识图谱数据\\中型标签分类.xls', 'ope', list_ope)
write_sheet_xls('C:\\CHINO\\NATSUME\\Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\高处坠落知识图谱数据\\中型标签分类.xls', 'env', list_env)
