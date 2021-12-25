import csv, io, sys, zipfile

zip_file = zipfile.ZipFile('voyna-i-mir.zip')
items_file  = zip_file.open('voyna-i-mir.txt', 'r')
# items_file.readable = lambda: True
# items_file.writable = lambda: False
# items_file.seekable = lambda: False
# items_file.read1 = items_file.read
items_file  = io.TextIOWrapper(items_file)

for idx, row in enumerate(csv.DictReader(items_file)):
    print('Processing row {0} -- row = {1}'.format(idx, row))


