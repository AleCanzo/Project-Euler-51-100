from sympy import isprime
    
K = 26237
perc = 11

while perc > 10:
    N = 3
    l = []
    n = 1
    c = 0
    while n < pow(K,2):
        for i in range(4):
            if isprime(n):
                c += 1
            l.append(n)
            n = (N-1) + n
        N = N + 2
    l.append(n)
    perc = (c/len(l))*100
    print("perc = {}".format(perc))
    K = K + 2

print(K - 2)