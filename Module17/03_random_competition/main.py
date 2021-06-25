import random

team1=[]
for index in range(20):
    team1.append(round(random.uniform(0,10), 2))
print ('Очки участников первой команда: ',team1)

team2=[]
for index in range(20):
    team2.append(round(random.uniform(0,10), 2))
print ('Очки участников второй команды: ',team2)

for i in len(team1):
    print(i,team1[i])

