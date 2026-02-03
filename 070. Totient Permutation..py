import  numpy as np
from sympy import isprime, divisors
from math import gcd
from itertools import permutations


def totient(PHI, n):
    if n%2==0:
        if int(n/2)%2==0:
            if PHI[int(n/2)] == 0:
                PHI[n] = 2*totient(int(n/2))
                return PHI[n]
            else:
                return 2*PHI[int(n/2)]
        else:
            if PHI[int(n/2)] == 0:
                PHI[n] = totient(int(n/2))
                return PHI[n]
            else:
                return PHI[int(n/2)]
    elif isprime(n):
        return n-1
    else:
        x = divisors(n)[1]
        y = int(n/x)
        d = gcd(x, y)
        if PHI[x]!=0 and PHI[y]!=0 and PHI[d]!=0:
            PHI[n] = int((PHI[x]*PHI[y]*d)/PHI[d])
            return PHI[n]
        if PHI[x]==0 and PHI[y]!=0 and PHI[d]!=0:
            PHI[n] = totient(PHI, x)*PHI[y]*int(d/PHI[d])
            return PHI[n]
        if PHI[x]==0 and PHI[y]==0 and PHI[d]!=0:
            PHI[n] = totient(PHI, x)*totient(PHI, y)*int(d/PHI[d])
            return PHI[n]
        if PHI[x]==0 and PHI[y]!=0 and PHI[d]==0:
            PHI[n] = totient(PHI, x)*PHI[y]*int(d/totient(PHI, d))
            return PHI[n]
        if PHI[x]!=0 and PHI[y]==0 and PHI[d]!=0:
            PHI[n] = PHI[x]*totient(PHI, y)*int(d/PHI[d])
            return PHI[n]
        if PHI[x]!=0 and PHI[y]==0 and PHI[d]==0:
            PHI[n] = PHI[x]*totient(PHI, y)*int(d/totient(PHI, d))
            return PHI[n]
        if PHI[x]!=0 and PHI[y]!=0 and PHI[d]==0:
            PHI[n] = PHI[x]*PHI[y]*int(d/totient(PHI, d))
            return PHI[n]
        if PHI[x]==0 and PHI[y]==0 and PHI[d]==0:
            PHI[n] = totient(PHI, x)*totient(PHI, y)*int(d/totient(PHI, d))
            return PHI[n]
    
def perm(PHI, n):
    for x in permutations(str(n)):
        z = int(''.join(map(str, x)))
        if PHI[n] == z:
            return z
    return 0
    
PHI = np.zeros((10_000_001), int)
min = 10
PHI[1] = 1
PHI[2] = 1
for n in range(3, 10_000_001):
    PHI[n] = totient(PHI, n)
    print("phi({})={}".format(n, PHI[n]))
    z = perm(PHI, n)
    if z!=0:
        N = float(n/PHI[n])
        if N < min:
            print("phi({})={}".format(n, PHI[n]))
            min = N
            n_min = n
        
print(n_min)