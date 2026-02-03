max = 0

for a in range(1,100):
    for b in range(1,100):
        if len(list(map(int,list(str(pow(a,b)))))) == 1:
            x = pow(a,b)
        else:
            x = sum(list(map(int,list(str(pow(a,b))))))
        if x > max:
            max = x

print(max)

