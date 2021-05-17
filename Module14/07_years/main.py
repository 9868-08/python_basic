A=1911
B=2100

for num in range(A,B):
    count = 0
    for checkin_digit in str(num):
        for digit in str(num):
            if checkin_digit==digit:
                count+=1
            if count == 3:
                print(num)
                count = 0
        count = 0
        break
#print('итого:',result)