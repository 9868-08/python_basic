def print_site(site,quantity,name):
    print('Сайт для', name, ':\nsite = {')
    print(site.format(name))

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
    print_site(site,quantity,name)