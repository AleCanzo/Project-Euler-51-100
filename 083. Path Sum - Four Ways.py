from math import inf

def read_file(f):
    with open(f, 'r') as f:
        l = [[int(num) for num in line.split(',')] for line in f]
    return l

def min_node_weight(UNVISITED, PATH_WEIGHT):
    min = inf
    for v in UNVISITED:
        x , y = v
        if PATH_WEIGHT[x][y] < min:
            min = PATH_WEIGHT[x][y]
            u = v
    return u
        
def node_neighbours(u, N):
    x, y = u
    if x == 0:
        if y == 0:
            return [(x+1, y), (x, y+1)]
        elif y == N-1:
            return [(x+1, y), (x, y-1)]
        else:
            return [(x, y+1), (x, y-1), (x+1, y)]
        
    elif y == 0:
        if x == N-1:
            return [(x-1, y), (x, y+1)]
        else:
            return [(x+1, y), (x-1, y), (x, y+1)]
        
    elif x == N-1:
        if y == N-1:
            return [(x-1, y), (x, y-1)]
        else:
            return [(x-1, y), (x, y-1), (x, y+1)]
             
    elif y == N-1:
        return [(x+1, y), (x-1, y), (x, y-1)]
    
    else:
        return [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]

N = 80
f = "0081_matrix.txt"
NODE_WEIGHT = read_file(f)
UNVISITED = []
PATH_WEIGHT = []

for x in range(N):
    l = []
    for y in range(N):
        l.append(inf)
        UNVISITED.append((x,y))
    PATH_WEIGHT.append(l)
    
PATH_WEIGHT[0][0] = NODE_WEIGHT[0][0]
while len(UNVISITED) != 0:
    u = min_node_weight(UNVISITED, PATH_WEIGHT)
    neighbours = node_neighbours(u, N)
    for v in neighbours:
        vx , vy = v
        ux, uy = u
        d = PATH_WEIGHT[ux][uy] + NODE_WEIGHT[vx][vy]
        if d < PATH_WEIGHT[vx][vy]:
            PATH_WEIGHT[vx][vy] = d
    UNVISITED.remove(u)
    

print(PATH_WEIGHT[N-1][N-1])