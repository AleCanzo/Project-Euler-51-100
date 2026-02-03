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

dict = {}
N = 100
values = list(range(1,N)) + [N]
values.sort(reverse=True)
print(sums(values[0], tuple(values)) - 1)
