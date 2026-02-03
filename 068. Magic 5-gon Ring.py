from itertools import permutations
import numpy as np

def order_list(l):
    min = 11
    for x in l:
        if x[0] < min:
                min = x[0]
                i = l.index(x)
    for j in range(len(l)):
        if j+i<len(l):
            list[j]=l[j+i]
        else:
            list[j]=l[j+i-len(l)]
    return list

M = np.zeros((2,5), int)

max = 0
l = []
list = [0, 0, 0, 0, 0]
for t in permutations([1,2,3,4,5,6,7,8,9,10]):
    M[0,0] = t[0]
    M[0,1] = t[1]
    M[0,2] = t[2]
    M[0,3] = t[3]
    M[0,4] = t[4]
    M[1,0] = t[5]
    M[1,1] = t[6]
    M[1,2] = t[7]
    M[1,3] = t[8]
    M[1,4] = t[9]
    
    a = M[1,4] + M[0,3] + M[0,2]
    b = M[1,3] + M[0,2] + M[0,1]
    c = M[1,2] + M[0,1] + M[0,0]
    d = M[1,1] + M[0,0] + M[0,4]
    e = M[1,0] + M[0,4] + M[0,3]

    if a == b == c == d == e:
        x = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(M[1,4], M[0,3], M[0,2], M[1,3], M[0,2], M[0,1], M[1,2], M[0,1], M[0,0], M[1,1], M[0,0], M[0,4], M[1,0], M[0,4], M[0,3])
        l.append([int(M[1,4]), int(M[0,3]), int(M[0,2])])
        l.append([int(M[1,3]), int(M[0,2]), int(M[0,1])])
        l.append([int(M[1,2]), int(M[0,1]), int(M[0,0])])
        l.append([int(M[1,1]), int(M[0,0]), int(M[0,4])])
        l.append([int(M[1,0]), int(M[0,4]), int(M[0,3])])
        l = order_list(l)
        x="{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(l[0][0], l[0][1], l[0][2], l[1][0], l[1][1], l[1][2], l[2][0], l[2][1], l[2][2], l[3][0], l[3][1], l[3][2], l[4][0], l[4][1], l[4][2])
        if len(x) == 16:
            if int(x) > max:
                max = int(x)
        l = []

print(max)


