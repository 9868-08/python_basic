import zipfile
import os
import time
import chardet

import zipfile
with zipfile.ZipFile("voyna-i-mir.zip") as z:
   with z.open('voyna-i-mir.txt') as f:
    for line in f:
#        print (chardet.detect(line))
        print (line)
