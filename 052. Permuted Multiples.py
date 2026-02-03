Flag = False
n = 1
while Flag == False:
    c = 0
    l = list(str(n))
    l.sort()
    for k in range(1, 7):
        m = list(str(n*k))
        m.sort()
        if m == l:
            c = c + 1
    if c == 6:
        print(n)
        Flag = True
    n = n + 1   