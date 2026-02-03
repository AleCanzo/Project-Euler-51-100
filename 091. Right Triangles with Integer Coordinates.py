import math

def is_rect(coord):
    OP = (coord[0][0] - coord[1][0])**2 + (coord[0][1] - coord[1][1])**2
    OQ = (coord[0][0] - coord[2][0])**2 + (coord[0][1] - coord[2][1])**2
    PQ = (coord[1][0] - coord[2][0])**2 + (coord[1][1] - coord[2][1])**2
    ipo = max([OP, OQ, PQ])
    if ipo == OP:
        if OP == OQ + PQ:
            return True
        else:
            return False
    elif ipo == OQ:
        if OQ == OP + PQ:
            return True
        else:
            return False
    elif ipo == PQ:
        if PQ == OQ + OP:
            return True
        else:
            return False
  
N = 51
c = []

for i in range(N):
    for j in range(N):
        for h in range(N):
            for k in range(N):
                if (h,k) != (i,j) and (h,k) != (0,0) and (i,j) != (0,0):
                    if is_rect([(0,0), (h,k), (i,j)]):
                        c.append([(0,0), (h,k), (i,j)])

                 
print(int(len(c)/2))