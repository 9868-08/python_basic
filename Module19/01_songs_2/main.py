violator_songs = {
	'World in My Eyes': 4.86,
	'Sweetest Perfection': 4.43,
	'Personal Jesus': 4.56,
	'Halo': 4.9,
	'Waiting for the Night': 6.07,
	'Enjoy the Silence': 4.20,
	'Policy of Truth': 4.76,
	'Blue Dress': 4.29,
	'Clean': 5.83
}
# Напишите программу, которая запрашивает у пользователя кол-во песен из списка и затем названия этих песен, а на экран  выводит # общее время их звучания.
#print (violator_songs)
# count=int(input('Сколько песен выбрать? '))
count = 3
selected_songs = []
#selected_songs = ['Policy of Truth','Enjoy the Silence','Personal Jesus']
for i in range(0,count):
	selected_songs.append(input("Введте название песни: "))
playing_time = 0
for i in violator_songs:
	if i in selected_songs:
		playing_time += violator_songs[i]
print('Общее время звучанния', selected_songs, '=', playing_time)