
import  numpy as np
from sympy import isprime, divisors
from math import gcd


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
    
    
PHI = np.zeros((1000001), int)
max = 0
PHI[1] = 1
PHI[2] = 1
for n in range(3, 1000001):
    PHI[n] = totient(PHI, n)
    N = float(n/PHI[n])
    if N > max:
        max = N
        n_max = n
        
print(n_max)