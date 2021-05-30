films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

user_film='Мементо1'
favorite_films=[]
for film in films:
    if not film==user_film:
        favorite_films.append(film)
if not favorite_films:
  print("Лучших фильмов нет")
else:
    print('Список лучщих фильмов', favorite_films)