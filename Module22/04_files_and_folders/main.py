import os

print("C:/1/python_basic/Module22/04_files_and_folders/1")
dirname = input('Введите путь до каталога: ')
dirfiles = os.listdir(dirname)

fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)
dirs = []
files = []
for file in fullpaths:
    if os.path.isdir(file): dirs.append(file)
    if os.path.isfile(file): files.append(file)

print('В директории', dirname, len(list(dirs)), 'папок')
print('В директории', dirname, len(list(files)), 'файлов')
