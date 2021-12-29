import os


def sort_dict(def_dict):
    print (list (def_dict)[1])
    max = 0
   # print (max)
    for i in def_dict:
        if def_dict[i] > max:
            max = def_dict[i]
        #print('i=',i, 'def_dict[i]=', def_dict[i])
    return max


def get_lines(file_name):
    out = []
    with open(file_name, 'r') as input_file:
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
    #    fp = open(file_out, 'w')
    out_text = "Количество букв в файле:" + str(char_count) + "\n"
    #    file_out.write(out_text)
    #    print ('out_text=',out_text)
    out_text = "Количество слов в файле:" + str(words_count) + "\n"
    #    file_out.write(out_text)
    #    print ('out_text=',out_text)
    out_text = "Количество строк в файле:" + str(lines_count) + "\n"
    #    file_out.write(out_text)
    #    print ('out_text=',out_text)
    out_text = "Наиболее редкая буква:" + least_freq_char + "\n"
    #    print('out_text=', out_text)
    for i_word in letters_dict:
        out_text = i_word + ' ' + str(round(letters_dict[i_word] / char_count, 3)) + '\n'
        print('out_text=', out_text)
        file_out.write(out_text)
    sort_dict(letters_dict)
    return


def count_all_symbols(input_filename):
    char_count = 0
    letters_dict = dict()
    for line in get_lines(input_filename):
        chars_in_line, words_in_line = analyse_line(letters_dict, line)
        char_count += chars_in_line
    print(letters_dict)
    return char_count


def main(input_filename, out_file):
    input_filename = os.path.abspath(os.path.join('.', input_filename))
    file_for_write = open(os.path.abspath(os.path.join('.', out_file)), 'w')
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
    print(sort_dict(letters_dict))
    return


main('text.txt', 'analysis.txt')
