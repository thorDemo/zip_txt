# -*- coding:utf-8 -*-
import hashlib
from scrapy.utils.python import to_bytes
import os, shutil


dirPath = '/home/wwwroot/61k/public/Nicholas/img/'
for parent, dirnames, filename in os.walk(dirPath):
    temp = 0
    for name in filename:
        new_path = dirPath + str(temp // 300)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        img = os.path.join(parent, name)
        shutil.move(img, new_path)
        print(img)
        temp += 1