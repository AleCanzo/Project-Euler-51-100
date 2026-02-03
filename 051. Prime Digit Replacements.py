from sympy import isprime
import itertools

def return_comb(s, N):
    combinations = []
    for comb in itertools.combinations(range(0, len(s)), N):
        combinations.append(comb)
    return combinations

def max_list_primes(combinations, s):
    max = 0
    for comb in combinations:
        l = []
        num = list(s)
        for n in range(10):
            for i in range(len(comb)):
                num[comb[i]] = n
            x = int("".join(map(str, num)))
            if isprime(x) and len(str(x)) == len(num):
                l.append(x)
        if len(l) >= max:
            max_l = l
            max = len(l)
    return max_l
    
len_max = 0
n = 56000
while len_max != 8:
    for N in range(1, len(str(n)) + 1):
        combinations = return_comb(str(n), N)
        list_primes = max_list_primes(combinations, str(n))
        if len(list_primes) > len_max:
            print(list_primes)
            len_max = len(list_primes)
            if len(list_primes) == 8:
                len_max = 8  
    n += 1
    
    
    
          
