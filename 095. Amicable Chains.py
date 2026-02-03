import math

def Divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    if n in divisors:
        divisors.remove(n)
    return divisors

def amicable_chain(n):
    chain = [n]
    Flag = True
    while Flag == True:
        x = sum(Divisors(n))
        if x == chain[-1]:
            return False
        if x >= 1_000_000:
            return False
        if x not in chain:
            chain.append(x)
            n = x
        elif x in chain:
            i = chain.index(x)
            return chain[i:]
        
   
chains = []
for n in range(327600):
    chain = amicable_chain(n)
    if chain != False and len(chain)>1:
        if chain not in chains:
            chains.append(chain)        

max = 0
for c in chains:
    if len(c)>max:
        max = len(c)
        max_c = c

print(max_c, min(max_c))