from fractions import Fraction
import matplotlib.pyplot as plt

for m in range(7, 1_000):
    l = []
    for d in range(1, m):        
        for n in range(1, d):
            x = Fraction(n, d)
            l.append(x)
            #print(n, d, x)
    l = list(dict.fromkeys(l))
    #print(l)
    min = l[l.index(Fraction(3, 5)) - 1]
    
    print(l[l.index(Fraction(3, 5)) - 1])
    l.sort()

