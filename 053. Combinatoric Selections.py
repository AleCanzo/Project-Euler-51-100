from math import factorial

c = 0
for n in range(1, 101):
    for r in range(1, n):
        binom_n_r = factorial(n)/(factorial(r)*factorial(n - r))
        if binom_n_r >= 1000000:
            c += 1
            
print(c)