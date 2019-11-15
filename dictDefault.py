# -*- coding: utf-8 -*- 
# @Time : 2019/11/4 9:18 下午 
# @Author : Lian 
# @Site :  
# @File : dictDefault.py 
# @Software: PyCharm
import re


WORD_RE  = re.compile('\w+')

index = {}
with open('zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])

