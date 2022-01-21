import zipfile
import os
import time
import chardet
import zipfile

#encoding = 'utf-8'
'''with zipfile.ZipFile("voyna-i-mir.zip") as zfile:
    for name in zfile.namelist():
        with zfile.open("voyna-i-mir.txt") as readfile:
            for line in io.TextIOWrapper(readfile, encoding):
                print(repr(line))

'''

z = zipfile.ZipFile("voyna-i-mir.zip", 'r')  # self.read_f - путь к файлу
for file in z.namelist():
    z.extract(file, self.mkdir(file))