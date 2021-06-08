violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

count_songs=3               # Количество песен выбрать
input_songs=['Personal Jesus', 'Waiting for the Night', 'Policy of Truth']
input_songs_sound_time=0
for song_in_violator_songs in violator_songs:
    for song_in_input_songs in input_songs:
        if song_in_violator_songs[0]==song_in_input_songs:
            print('найдено совпадение песни', song_in_input_songs,'добавляется длительность',song_in_violator_songs[1])
            input_songs_sound_time+=song_in_violator_songs[1]
print('Общее время звучания песен:', input_songs,'равно',input_songs_sound_time)

