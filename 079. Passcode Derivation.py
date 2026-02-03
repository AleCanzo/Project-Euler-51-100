import numpy as np

keylog = np.loadtxt("0079_keylog.txt", dtype=int, delimiter=",")

l = []
for s in keylog:
    s = str(s)
    for n in s:
        if n not in l:
            l.append(n)
            
M = np.zeros((10, 10), dtype=int)
for n in l:
    for s in keylog:
        s = str(s)
        n = str(n)
        if n in s:
            i = s.index(n)
            #print(n, s, ":")
            for y in s:
                if s.index(y) < i:
                    #print(s, n, y)
                    n = int(n)
                    y = int(y)
                    M[n][y] = -1
                elif s.index(y) > i:
                    #print(s, n, y)
                    n = int(n)
                    y = int(y)
                    M[n][y] = 1

l = np.zeros(10, dtype=int)
for i in range(10):
    c = 0
    for j in range(10):
        if M[i][j] == 1:
            c += 1
    l[i] = c

max = np.max(l)
code = []
while max >= 0:
    code.append(list(l).index(max))
    max = max - 1
    
print(int("".join(map(str, code))))
