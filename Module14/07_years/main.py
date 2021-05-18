start=1900
last_year=start-1
end=2100

for year in range(start,end):      #перебираем года
    count = 0
    for external_cycle_digit in str(year):    #перебираем цифры в числе - год
        for internal_cycle_digit in str(year):    #и сравниваем с каждой другой цифрой года
            if internal_cycle_digit==external_cycle_digit:
                count+=1
            if count == 3 and last_year!=year:
                print(year)
                count = 0
                last_year=year
        count = 0

