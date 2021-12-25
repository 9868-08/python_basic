import os


def get_file_path(file_name):
    return os.path.abspath(os.path.join('.', file_name))


def get_lines(file_name):
    file_path = get_file_path(file_name)
    out = []
    with open(file_path, 'r') as input_file:
        out += input_file.readlines()[::-1]
    return out


def analyse_line(letters_dict, line):
    char_count = 0
    for char in line.lower():
        if 'a' <= char <= 'z':
            if char not in letters_dict:
                letters_dict[char] = 0
            letters_dict[char] += 1
            char_count += 1
    words_count = len(line.split(' '))
    return char_count, words_count


def get_min_freq_char(items):
    min_freq = 0
    keys = list(items)
    min_freq_char = keys[0][0]
    for item in items:
        if item[1] < min_freq:
            min_freq = item[1]
            min_freq_char = item[0]
    return min_freq_char


def print_results(char_count, words_count, lines_count, least_freq_char, letters_dict, file_out):
    filename_output = str(get_file_path(file_out)) + file_out
    print(filename_output)
    print("Количество букв в файле:", char_count)
    write_to_file(filename_output, "Количество букв в файле:" + char_count)
    print("Количество слов в файле:", words_count)
    print("Количество строк в файле:", lines_count)
    print("Наиболее редкая буква:", least_freq_char)
    return

def count_all_symbols(input_filename):
    char_count = 0
    letters_dict = dict()
    for line in get_lines(input_filename):
        chars_in_line, words_in_line = analyse_line(letters_dict, line)
        char_count += chars_in_line
        print (letters_dict)
    return char_count

def main(input_filename, out_file):
    file_for_write = open(out_file, 'w')
    lines_count = 0
    char_count = 0
    words_count = 0
    letters_dict = dict()
    for line in get_lines(input_filename):
        chars_in_line, words_in_line = analyse_line(letters_dict, line)
        char_count += chars_in_line
        words_count += words_in_line
        lines_count += 1
    least_freq_char = get_min_freq_char(letters_dict.items())

    print_results(count_all_symbols(input_filename), words_count, lines_count, least_freq_char, letters_dict,
                  file_for_write)
    #    print (count_all_symbols(input_filename))
    return


main('text.txt', 'analysis.txt')
