"""
author:chimamo  https://github.com/CHIMAMO
date:2022-08-25
把不要的标签变成O
"""


def delete_tags(path, old_file, new_file):
    list_a = []
    list_tag = ['B-lbs', 'B-gov', 'B-ope', 'B-env', 'B-ust', 'B-ins', 'B-opr', 'B-ppt', 'B-che', 'B-equ',
                'I-lbs', 'I-gov', 'I-ope', 'I-env', 'I-ust', 'I-ins', 'I-opr', 'I-ppt', 'I-che', 'I-equ'
                ]

    with open(path + old_file, 'r', encoding='utf-8') as f:
        for line in f:
            a = line.strip().split('\t')
            if len(a) == 1:
                list_a.append(a)
            if len(a) == 2:
                if a[1] in list_tag:
                    a[1] = 'O'
                    list_a.append(a)
                else:
                    list_a.append(a)
    with open(path + new_file, 'w', encoding='utf-8') as p:
        for j in list_a:
            if len(j) == 2:
                p.write(j[0] + '\t' + j[1] + '\n')
            else:
                p.write('\n')


delete_tags(r'C:\\CHINO\\NATSUME\\'
           'Postgraduate\\Research\\论文撰写\\高处坠落论文及实验\\'
           'LANN处理后BIO及BMES数据\\test_1\\', 'BIO_update_file.txt', 'BIO_update_file_delete.txt')
