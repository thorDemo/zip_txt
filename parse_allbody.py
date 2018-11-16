# -*- coding:utf-8 -*-
import hashlib
from scrapy.utils.python import to_bytes
import os, shutil


targetPath = 'target'
dirPath = 'content'
file = open('target/all_body.txt', 'w+', encoding='utf-8')
web_name = open('target/web_name.txt', 'w+', encoding='utf-8')
for parent, dir_names, filename in os.walk(dirPath):
    for name in filename:
        txt = os.path.join(parent, name)
        parse_txt = open(txt, 'r+', encoding='utf-8')
        file.write(name.strip('.txt') + '##########')
        web_name.write(name.strip('.txt') + '\n')
        for line in parse_txt:
            file.write(line.strip().strip('\n'))
        file.write('\n')
