from sympy import isprime

def sums(v, values):
    values = list(values)
    c = 0
    while len(values)!= 0:
        u = values[0]
        if u < v:
            if (v - u, tuple(values[:])) in dict:
                c = c + dict[(v - u, tuple(values[:]))]
            else:
                x = sums(v - u, values[:])
                c = c + x
                dict[(v - u, tuple(values[:]))] = x
            values.remove(u)
        elif u == v:
            c = c + 1
            values.remove(u)
        elif u > v:
            values.remove(u) 
    return c

x = 0
N = 50
  
while x < 5000:
    dict = {}
    values = list(range(1,N)) + [N]
    values.sort(reverse=True)
    values = [x for x in values if isprime(x)]
    x = sums(values[0], tuple(values)) - 1
    N += 1

print(N-1)