def make_site(name):  # name - имя товара
    # struct_site = copy.deepcopy(site)
    struct_site = site.copy()  # надо будет импортировать copy
    # ^ два варианта копирования, т.е. берём уже имеющуюся структуру, создаём копию её и закрепляем за переменной struct_site

    new_title = 'Куплю/продам {} недорого'.format(name)  # новая строка

    struct_site = change_value(struct_site, 'title',
                               new_title)  # функция change_value будет идти по struct_site и заменять по ключу title строку на строку выше
    new_h2 = 'У нас самая низкая цена на {}'.format(name)  # то же самое что и выше
    struct_site = change_value(struct_site, 'h2', new_h2)

    return struct_site  # делаем возврат

# функция change_value будет идти по struct_site и заменять по ключу title строку на строку выше
def change_value(struct_site, 'title', new_title):
    for i_key,i_value in struct_site:
        if i_key == 'title':
            struct_site[i_key] = new_title

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {}',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

quantity = int(input('Количество сайтов: '))
for i_site in range(0,quantity):
    name = input('Введите название продукта для нового сайта: ')
    print(make_site(name))