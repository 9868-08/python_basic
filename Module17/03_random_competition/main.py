import random

team1=[]
team1 = [round(random.uniform(0,10),2) for i in range(20)]
print ('Очки участников первой команды: ',team1)

team2 = [round(random.uniform(0,10),2) for i in range(20)]
print ('Очки участников второй команды: ',team2)

team3 = [team1[i] for i in range(20) if team1[i]>team2[i]]
team3 = [team2[i] for i in range(20) if team1[i]>team2[i]]

print ('Очки участников побед-лей тура: ',team3)
