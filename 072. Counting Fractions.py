from fractions import Fraction
from math import gcd

def coprime(n):
    return [k for k in range(1, int(n/2) + 1) if gcd(k, n) == 1]

if __name__ == "__main__":
    c = 0
    for d in range(12_001):
        for x in coprime(d):
            y = Fraction(x, d)
            if y > Fraction(1, 3) and y < Fraction(1, 2):
                c += 1
    print(c)