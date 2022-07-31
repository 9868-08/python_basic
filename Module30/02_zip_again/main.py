from typing import List

def f(x,y):
    return  [x,y]

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print ("via zip function:", list(zip(letters,numbers)))

result  = map(lambda x,y: [y,x], numbers, letters)
print("via 1 line code   ", list(result))


# result: List[str] = list(map(lambda x, y: [x, str(y - 1)], letters, numbers))
#result: List[str] = list(map(f(x, y)))

#print(result)
