guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while 1:
    inc = input('ушёл кто-то или пришёл новый? ')
    lst = inc.split()  # ушел Петя
    if lst[0]=='ушел':
        if lst[1] in guests:
            guests.remove(lst[1])
    elif lst[0]=='пришел':    # пришел Алеша
        if len(guests)<6:
            guests.append(lst[1])
    elif lst[0]=='Пора' and lst[1]=='спать':
        break
    print('На вечеринке',len(guests),'человек. В гостях остались:',guests)
print('Вечеринка закончилась, все легли спать.')