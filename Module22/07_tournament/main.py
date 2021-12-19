import os

def get_file_path(file_name):
    return os.path.abspath(os.path.join('.', file_name))

def get_input(file_path):
    with open(file_path, 'r') as input_file:
        k_score = int(input_file.readline())

        persons = []
        for line in input_file.readlines()[1:]:
            last_name, first_name, score = line.split(' ')
            score = int(score)
            persons.append((first_name, last_name, score))

    return k_score, persons

def write_output(output_file_path, sorted_persons):
    with open(output_file_path, 'w') as output_file:
        output_file.write('{:d}\n'.format(len(sorted_persons)))

        for i, (first_name, last_name, score) in enumerate(sorted_persons):
            output_file.write('{:d}) {:s}. {:s} {:d}\n'.format(i + 1, first_name, last_name, score))

def get_person_score(person):
    return person[2]

def main(input_filename, output_filename):
    input_file_path = get_file_path(input_filename)
    output_file_path = get_file_path(output_filename)

    k_score, persons = get_input(input_file_path)
    persons = [p for p in persons if not isinstance(p[1], p else (p[1],p))

    persons.sort(key=get_person_score, reverse=True)

    write_output(output_file_path, persons)

main('first_tour.txt', 'second_tour.txt')