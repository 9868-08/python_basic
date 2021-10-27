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


def f(dict):
    lst = []
    last_name_len = 0
    for i in dict:
        lst += (dict[i]['interests'])
        last_name_len += len(dict[i]['surname'])
    cnt = 0
    return lst, last_name_len

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
