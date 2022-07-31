import zipfile
import os
import time
import chardet
import zipfile

with zfile.open("voyna-i-mir.zip", 'rU') as readFile:
    line = readFile.readline().decode('utf8')
    # etc

'''with zipfile.ZipFile("voyna-i-mir.zip") as z:
   with z.open('voyna-i-mir.txt', 'r', encoding='utf-8') as f:
    for line in f:
#        print (chardet.detect(line))
        print (line)
'''