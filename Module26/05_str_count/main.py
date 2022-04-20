import os


def check_py_files(def_search_dir):
    files = os.listdir(def_search_dir)
    print(files)
    for f in files:
        lines_count = 0
        print(def_search_dir+"/"+f)

        if f[-2:] == "py":
            with open(def_search_dir+"/"+f) as file:
                for line in f:
                    if line != "#\n" and line != "\n":     # игнорирую строчки с комментарием
                        lines_count += 1
                print('в фале {} {} строчек кода'.format(f, lines_count))



check_py_files("../01_num_squares")