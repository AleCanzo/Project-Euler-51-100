from math import isqrt

def continued_fraction_sqrt(n):
    m = 0
    d = 1
    a0 = isqrt(n)
    if a0 * a0 == n:  
        return [a0], []

    a = a0
    period = []
    seen = set()

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        if (m, d, a) in seen:  
            break
        seen.add((m, d, a))
        period.append(a)

    return [a0], period

c = 0
for n in range(10001):
        a0, period = continued_fraction_sqrt(n)
        if len(period) %2 !=0:
                c += 1
print(c)


        
                

