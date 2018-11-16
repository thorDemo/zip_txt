# -*- coding:utf-8 -*-
import hashlib
from scrapy.utils.python import to_bytes
import os, shutil


targetPath = 'target'
dirPath = 'content'
for parent, dirnames, filename in os.walk(dirPath):
    for name in filename:
        img = os.path.join(parent, name)
        images = hashlib.sha1(to_bytes(img)).hexdigest() + '.jpg'
        print(img, images)
        shutil.copy(img, targetPath + '/' + images)
