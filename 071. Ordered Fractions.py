from fractions import Fraction
from math import gcd

if __name__ == "__main__":
    min = Fraction(2,5)
    m, n = 2, 5
    while n <= 1_000_001:
        y = Fraction(m, n)
        if y >= min and y < Fraction(3, 7):
            min = y
        n += 7
        m += 3
    print(min)

