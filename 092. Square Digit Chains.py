def chain_with_89(n):
    n = str(n)
    sum = 0
    for x in n:
        x = int(x)
        sum = sum + pow(x, 2)
    if sum == 89:
        return True
    if sum == 1:
        return False
    else:
        return chain_with_89(sum)

c = 0
for n in range(1, 10000000):    
    if chain_with_89(n):
        c += 1 

print(c)