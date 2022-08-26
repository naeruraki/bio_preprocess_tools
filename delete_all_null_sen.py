"""
author:chimamo  https://github.com/CHIMAMO
date:2022-08-25
删除全O语句
"""


def delete_all_null_sen(path, old_file, new_file):
    list_a = []
    list_b = []
    list_tmp = []

    with open(path + old_file, 'r', encoding='utf-8') as f:
        for line in f:
            a = line.strip().split('\t')
            if len(a) == 2:
                list_a.append(a)
            if len(a) == 1:
                for p in list_a:
                    list_tmp.append(p[1])
                if len(set(list_tmp)) == 1:
                    list_a = []
                    list_tmp = []
                else:
                    for q in list_a:
                        list_b.append(q)
                    list_b.append('')
                list_a = []
                list_tmp = []

    with open(path + new_file, 'w', encoding='utf-8') as p:
        for j in list_b:
            if len(j) == 2:
                p.write(j[0] + '\t' + j[1] + '\n')
            else:
                p.write('\n')


delete_all_null_sen(r'C:\\CHINO\\NATSUME\\'
                    'Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\'
                    'LANN处理后BIO及BMES数据\\test_1\\', 'BIO_update_file_delete.txt', 'BIO_no_null.txt')
