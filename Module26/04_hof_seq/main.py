class qsequence:
    def __init__(self, s):
        self.s = s[:]

    def __next__(self):
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self

    def current_state(self):
        return self.s

    def __str__(self):
        for item in self.s:
            print(item, end=" ")


Q = qsequence([1, 1])
result = list()
for count in range(3, 15):
    result.append(next(Q))
print(result)
try:
    print(Q)
except TypeError:
    print()

