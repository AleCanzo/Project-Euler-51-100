from sympy import isprime, divisors



#print("fatto")

"""list_p = []
l = divisors(50000000)
for x in l:
    if isprime(x):
        print(x)
        list_p.append(x)
        
print(list_p, pow(2,7)*pow(5,8))"""

"""i = 0
p = list_primes[i]
f = pow(p,4) + pow(p,3) + pow(p,2) - 50000000
while f <= 0:
    p = list_primes[i]
    f = pow(p,4) + pow(p,3) + pow(p,2) - 50000000
    print("{}: valore = {}".format(p, f))
    i += 1"""
#print(pow(5,4))


list_primes=[]
for i in range(1,5000):
    if isprime(i):
        list_primes.append(i)
        #print(i)

l = []
N = 50_000_000
count = 0
for x in reversed(list_primes):
    for y in reversed(list_primes):
        if pow(x,4) + pow(y,3) < N:
            for z in reversed(list_primes):
                f = pow(x,4) + pow(y,3) + pow(z,2)
                if f < N:
                    print(x, y, z, f)
                    count += 1
                    t = (x, y, z, f)
                    l.append(t)

senza_duplicati = list(set(l))
print(len(senza_duplicati))                    
print(count)
        




