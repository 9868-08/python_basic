from typing import List

def can_be_poly(x):
    return list(filter(lambda x: (x == "".join(reversed(x))), texts))

texts = ["abcba", 'abbbc']
print("Orginal list of strings:")
print(texts)
result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
print("\nList of palindromes:")
print(result)


