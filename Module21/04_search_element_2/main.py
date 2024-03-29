def find_key(struct, key, searching_deep=2):
	if key in struct:
		return struct[key]

	for sub_struct in struct.values():
		if searching_deep == 0:
			print('достингута максимальная глубина поиска')
			return None
		if isinstance(sub_struct, dict):
			searching_deep -= 1
			result = find_key(sub_struct, key, searching_deep)
			if result:
				break
	else:
		result = None
	return result

site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

searching_key = 'body'

value = find_key(site, searching_key)
if value:
	print(value)
else:
	print('Такого ключа в структуре сайта нет.')