import zipfile
import os
import time
import chardet
import zipfile

encoding = 'utf-8'
with zipfile.ZipFile("voyna-i-mir.zip") as zfile:
    for name in zfile.namelist():
        with zfile.open("voyna-i-mir.txt") as readfile:
            for line in io.TextIOWrapper(readfile, encoding):
                print(repr(line))

'''with zipfile.ZipFile("voyna-i-mir.zip") as z:
   with z.open('voyna-i-mir.txt', 'r', encoding='utf-8') as f:
    for line in f:
#        print (chardet.detect(line))
        print (line)
'''
