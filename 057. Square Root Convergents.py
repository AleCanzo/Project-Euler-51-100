from fractions import Fraction
import sys

sys.setrecursionlimit(2000)

def f(n):
    if n == 1:
        return Fraction(1,2)
    else:
        return Fraction(1,(2 + f(n-1)))


c = 0
for n in range(1,1001):
    fract = 1 + f(n)
    if len(str(fract.numerator))>len(str(fract.denominator)):
        c += 1
print(c)
    
    