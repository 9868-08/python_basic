import os
from _collections_abc import Iterable


def scan_dir(path):
    #    return list(map(os.path.abspath, os.listdir(path)))
    return os.listdir(path)


def gen_files_path(def_search_dir, def_dir_to_find):
    dir_list = scan_dir(def_search_dir)
    for dir_in_path in dir_list:
        if dir_in_path == def_dir_to_find:
            for founded_dir in scan_dir(def_search_dir + dir_in_path):
                print("find {} in {}".format(founded_dir, def_search_dir + def_dir_to_find))
        else:
            print("Worked. Doesn't fit in ", dir_in_path)


search_dir = 'C:/1/python_basic/Module26/'
dir_to_find = "03_files_path"
gen_files_path(search_dir, dir_to_find)
