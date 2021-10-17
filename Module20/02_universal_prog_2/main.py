students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


#def f(dict):
#    return ([i for i in dict += (dict[i]['interests'])], [i for i in dict += (dict[i][
#    'interests'])])

def f(iter_obj):
        return [value for index, value in dict(iter_obj, start=0) if isPrime(index)]

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def Prime_set(inc):
	out_dic = dict()
	for i in inc:
		if isPrime(i):
			print(i)
			out_dic[i] = inc[i]
	print(out_dic)

pairs = dict ()
for i in students:
    pairs[i] = students[i]['age']
print('айди -    возраст')
for i in pairs:
    print(i,'   -   ', pairs[i])

global_lst = f(students)[0]
len = f(students)[1]
print('список интересов:',global_lst, '\nобщая длина всех фамилий:' , len)
print(Prime_set(students))
