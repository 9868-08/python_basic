import os

def write_to_file(filename, text):
	out_file = open(output_file, 'w')
	out_file.write(test_line)
	out_file.close()

test_line = 'testiruyem'
output_folder = '1 python_basic Module22 05_save'
output_folder = output_folder.split(' ')
output_f = 'my_document'

print('введены следующие данные:')
print('Куда сохранить документ:', output_folder)
print('Имя файла:', output_f)
output_file = 'c:/'
for item in output_folder:
	output_file = output_file + item + '/'
output_file = output_file + output_f
if os.path.exists(output_file):		# check dir exist
	print('файл существует')
	replace_quistion = input('Вы действительно хотите перезаписать файл? Y/N: ')
	if replace_quistion.lower() == 'y':
		print('перезаписываю')
		write_to_file(output_file, test_line)
else:
	write_to_file(output_file, test_line)
