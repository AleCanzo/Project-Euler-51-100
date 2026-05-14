from fractions import Fraction
import matplotlib.pyplot as plt

l = []
for d in range(1, 8):        
    for n in range(1, d):
        x = Fraction(n, d)
        l.append(x)
        print(n, d, x)
l = list(dict.fromkeys(l))
#print(l)
l.sort()
#print("Lista ordinata:\n")
#print(l)
"""x = range(len(l))
plt.plot(x, l)    
plt.show()    """