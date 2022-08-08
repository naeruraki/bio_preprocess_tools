"""
author:chimamo  https://github.com/CHIMAMO
date:2022-08-08
处理生成BIO文件
"""

'''
修改有误处
'''


def update_file(path, old_file, new_file):
    list_a = []
    list_tag = ["O",
                'B-opr', 'B-ppt', 'B-emr', 'B-che', 'B-def', 'B-lbs', 'B-equ', 'B-gov',
                'B-ust', 'B-edt', 'B-ins', 'B-ope', 'B-env',
                'I-opr', 'I-ppt', 'I-emr', 'I-che', 'I-def', 'I-lbs', 'I-equ', 'I-gov',
                'I-ust', 'I-edt', 'I-ins', 'I-ope', 'I-env']
    with open(path + old_file, 'r', encoding='utf-8') as f:
        for line in f:
            a = line.strip().split('\t')
            if len(a) > 2:
                continue
            else:
                list_a.append(a)

        for i in list_a:
            if len(i) != 1:
                if i[1] not in list_tag:
                    i[1] = 'O'

    with open(path + new_file, 'w', encoding='utf-8') as p:
        for j in list_a:
            if len(j) == 2:
                p.write(j[0] + '\t' + j[1] + '\n')
            else:
                p.write('\n')


'''
检查是否有误
'''


def check_file(path, new_file):
    list_tag = ["O",
                'B-opr', 'B-ppt', 'B-emr', 'B-che', 'B-def', 'B-lbs', 'B-equ', 'B-gov',
                'B-ust', 'B-edt', 'B-ins', 'B-ope', 'B-env',
                'I-opr', 'I-ppt', 'I-emr', 'I-che', 'I-def', 'I-lbs', 'I-equ', 'I-gov',
                'I-ust', 'I-edt', 'I-ins', 'I-ope', 'I-env']
    with open(path + new_file, 'r', encoding='utf-8') as f:
        for line in f:
            a = line.strip().split('\t')
            if len(a) > 2:
                print(a)
            if len(a) == 2:
                if a[1] not in list_tag:
                    print(a)

update_file(r'C:\\CHINO\\NATSUME\\'
           'Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\'
           'LANN处理后BIO及BMES数据\\20220808\\', 'BIO20220808.txt', 'BIOnew.txt')
check_file(r'C:\\CHINO\\NATSUME\\'
           'Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\'
           'LANN处理后BIO及BMES数据\\20220808\\', 'BIOnew.txt')