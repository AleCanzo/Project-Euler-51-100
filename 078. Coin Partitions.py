import numpy as np

def g(k):
    return int(k*(3*k - 1)/2)

def p(n):
    if n == 0:
        return 1
    total = 0
    k = 1
    while True:
        g1 = k * (3*k - 1) // 2
        g2 = k * (3*k + 1) // 2
        if g1 > n and g2 > n:
            break
        sign = -1 if k % 2 == 0 else 1
        if g1 <= n:
            total += sign * P[n - g1]
        if g2 <= n:
            total += sign * P[n - g2]
        k += 1
    return total

P = [0] * 100000  
P[0] = 1
n = 1
while True:
    P[n] = p(n)
    print("p({}) = {}".format(n, P[n]))
    """ n == 1000"""
    if P[n] % 1000000 == 0:
        break
    n += 1


print("Trovato", n, P[n])
            