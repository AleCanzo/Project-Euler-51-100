from fractions import Fraction
import sys

sys.setrecursionlimit(2000)

def f(l, i):
    if i != len(l) - 1:
        return Fraction(1, l[i] + f(l, i + 1))
    else:
        return 0

l = [1, 2]
k = 2 
for i in range(1, 99):
    if i % 3 == 0:
        l.append(2*k)
        k = k + 1
    else:
        l.append(1)

x = 2 + f(l, 0)
y = sum(list(map(int, str(x.numerator))))
print(y)