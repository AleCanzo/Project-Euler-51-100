
N = 500
c = 0

for x in range(1, N):
    for y in range(1, N):
        if len(str(pow(x, y))) == y:
            c += 1
print(c)