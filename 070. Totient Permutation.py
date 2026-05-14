from sympy.functions.combinatorial.numbers import totient

min = 10

def is_permutation(n1, n2):
    s1, s2 = str(n1), str(n2)
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

for n in range(3, 10_000_001):
    phi = totient(n)
    if is_permutation(phi, n):
        N = float(n/phi)
        if N < min:
            min = N
            n_min = n
        
print(n_min)