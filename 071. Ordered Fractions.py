from fractions import Fraction
import matplotlib.pyplot as plt

l = []
for d in range(1, 1_000_000):        
    for n in range(1, d):
        x = Fraction(n, d)
        l.append(x)
        #print(n, d, x)
l = list(dict.fromkeys(l))

l.sort()
print(l)
