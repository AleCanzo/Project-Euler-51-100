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

max = 0
c = 0
for n in range(2, 1001):
    a0, period = continued_fraction_sqrt(n)
    if len(period) != 0:
        a = a0 + period
        h = []
        k = []
        for i in range(100):
            if i>=2:
                h.append(a[i % (len(period)+1)]*h[i-1] + h[i-2])
                k.append(a[i % (len(period)+1)]*k[i-1] + k[i-2])
            elif i == 0:
                h.append(a[0])
                k.append(1)
            elif i == 1:
                h.append(a[i]*h[0] + 1)
                k.append(a[i]*k[0])
        r = len(period)
        if (r) %2 == 0:
            if r == 0:
                (x, y) = (1, 0)
            else:
                (x, y) = (h[r-1], k[r-1])
        else:
            (x, y) = (h[(2*r)-1], k[(2*r)-1])
    if x >= max:
        max = x
        max_d = n
        
print(max_d)           



        
                

