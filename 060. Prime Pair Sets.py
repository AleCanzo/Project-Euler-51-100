from sympy import isprime

def prime_concat(x, y):
    x = str(x)
    y = str(y)
    n = int(x + y)
    m = int(y + x)
    if isprime(n) and isprime(m):
        return True
    else:
        return False

N = 10000

list_primes = []
for n in range(3, N, 2):
    if isprime(n):
        list_primes.append(n)

l = []

#couples
for x in list_primes:
    for y in list_primes:
        if prime_concat(x, y) and tuple(sorted((x, y))) not in l:
            l.append(tuple(sorted((x, y))))

#triplets    
for x in list_primes:
    for y in l:
        if prime_concat(x, y[0]) and prime_concat(x, y[1]) and len(y)!=3 and tuple(sorted((x,) + y)) not in l:
            l.append(tuple(sorted((x,) + y)))
            
#removing couples
l = [t for t in l if len(t) != 2]

#quadruplets
for x in list_primes:
    for y in l:
        if prime_concat(x, y[0]) and prime_concat(x, y[1]) and prime_concat(x, y[2]) and len(y)!=4 and tuple(sorted((x,) + y)) not in l:
            l.append(tuple(sorted((x,) + y)))

#removing triplets  
l = [t for t in l if len(t) != 3]

for x in list_primes:
    for y in l:
        if prime_concat(x, y[0]) and prime_concat(x, y[1]) and prime_concat(x, y[2]) and prime_concat(x, y[3]) and len(y)!=5 and tuple(sorted((x,) + y)) not in l:
            l.append(tuple(sorted((x,) + y)))

#removing qudruplets  
l = [t for t in l if len(t) != 4]   

min = 10000000000
for y in l:
    if len(y) == 5:
        if sum(list(y)) < min:
            min = sum(list(y))

print(min)
