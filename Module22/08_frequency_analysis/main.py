import os


def sort_dict(def_dict):            # сортируем словарь по значениям
    def_dict_result = dict ()
    def_dict_result = {k: v for k, v in sorted(def_dict.items(), key=lambda item: item[1], reverse=True)}
#    print('def_dict_result=', def_dict_result)
    return def_dict_result


def file_read_all(file_input):
    out = []
    with open(file_input, 'r') as file_input_raw:
        out += file_input_raw.readlines()[::-1]
    file_input_raw.close
    return out


def line_analize(letters_dict, line):
    char_count_global = 0
    for char in line.lower():
        if 'a' <= char <= 'z':
            if char not in letters_dict:
                letters_dict[char] = 0
            letters_dict[char] += 1
            char_count_global += 1
    words_count = len(line.split(' '))
    return char_count_global, words_count

def print_results(file_out, letters_dict, char_count_global, words_count, lines_count):
    dict_sorted = sort_dict(letters_dict)
    for i_word in dict_sorted:
        out_text=i_word + ' ' + str(round(dict_sorted[i_word]/char_count_global,3)) + '\n'
#        print('out_text=', out_text[:len(out_text) - 1])
        file_out.write(out_text)

    return


def count_all_symbols(filename_input):
    char_count_global = 0
    letters_dict = dict()
    for line in read(filename_input):
        chars_in_line, words_in_line = line_analize(letters_dict, line)
        char_count_global += chars_in_line
    # print(letters_dict)
    return char_count_global


def main(filename_input, out_file):
    filename_input = os.path.abspath(os.path.join('.', filename_input))
    filename_output = open(os.path.abspath(os.path.join('.', out_file)), 'w')
    lines_count = 0
    char_count_global = 0
    words_count = 0
    letters_dict = dict()

    for line in file_read_all(filename_input):
        chars_in_line, words_in_line = line_analize(letters_dict, line)
        char_count_global += chars_in_line
        words_count += words_in_line
        lines_count += 1
    print_results(filename_output, sort_dict(letters_dict), char_count_global, words_count, lines_count)
    filename_output.close
    return


main('text.txt', 'analysis.txt')
